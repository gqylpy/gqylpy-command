"""
─────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████───████████──████████─██████─────────██████████████─████████──████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░░░██──██░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░██──██░░░░██─
─██░░██████████─██░░██████░░██───████░░██──██░░████─██░░██─────────██░░██████░░██─████░░██──██░░████─
─██░░██─────────██░░██──██░░██─────██░░░░██░░░░██───██░░██─────────██░░██──██░░██───██░░░░██░░░░██───
─██░░██─────────██░░██──██░░██─────████░░░░░░████───██░░██─────────██░░██████░░██───████░░░░░░████───
─██░░██──██████─██░░██──██░░██───────████░░████─────██░░██─────────██░░░░░░░░░░██─────████░░████─────
─██░░██──██░░██─██░░██──██░░██─────────██░░██───────██░░██─────────██░░██████████───────██░░██───────
─██░░██──██░░██─██░░██──██░░██─────────██░░██───────██░░██─────────██░░██───────────────██░░██───────
─██░░██████░░██─██░░██████░░████───────██░░██───────██░░██████████─██░░██───────────────██░░██───────
─██░░░░░░░░░░██─██░░░░░░░░░░░░██───────██░░██───────██░░░░░░░░░░██─██░░██───────────────██░░██───────
─██████████████─████████████████───────██████───────██████████████─██████───────────────██████───────
─────────────────────────────────────────────────────────────────────────────────────────────────────

Copyright (c) 2022 GQYLPY <http://gqylpy.com>. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import sys
import builtins

from subprocess import Popen, TimeoutExpired

mswindows, bytes_output_end_sign, bytes_output_end_point = \
    (True, b'\r\n', -2) if sys.platform == 'win32' else (False, b'\n', -1)


class GqylpyCommand:
    PIPE, STDOUT, DEVNULL = -1, -2, -3

    def __init__(
            self,
            *cmdline,

            stdin:  int = -1,
            stdout: int = -1,
            stderr: int = -1,

            shell:   bool = True,
            cwd:     str  = None,
            env:     dict = None,
            bufsize: int  = -1,

            text:               bool = True,
            universal_newlines: bool = True,

            input:         'bytes | str' = None,
            timeout:        int          = None,
            ignore_timeout: bool         = False,

            **other_hardly_used_params
    ):
        # That is maintained here for backwards compatibility. The parameters
        # vary  between versions, only one commonly used parameter is maintained
        # here, in  fact there are many more.
        if not text and universal_newlines:
            universal_newlines = False

        if input is None:
            # Explicitly passing input=None was previously equivalent to passing
            # an empty string. That is maintained here for backwards
            # compatibility.
            input = '' if universal_newlines else b''
        elif stdin is not self.PIPE:
            raise ValueError(
                'when the argument "input" is specified, '
                'the argument "stdin" must be "PIPE(-1)".'
            )

        with Popen(
                cmdline, stdin=stdin, stdout=stdout, stderr=stderr,
                shell=shell, cwd=cwd, env=env, bufsize=bufsize,
                universal_newlines=universal_newlines,
                **other_hardly_used_params
        ) as process:
            try:
                self.stdout, self.stderr = process.communicate(input, timeout)
            except TimeoutExpired as e:
                process.terminate()
                # Windows and other systems handle this differently.
                if mswindows:
                    e.stdout, e.stderr = process.communicate()
                else:
                    process.wait()
                if not ignore_timeout:
                    raise
                self.code = 1
                self.stdout = None
                self.stderr = None
            except:
                process.terminate()
                raise
            else:
                self.code = process.poll()

        self.cmdline = cmdline
        self.universal_newlines = universal_newlines

    @property
    def cmd(self) -> str:
        return ''.join(self.cmdline)

    def raise_if_error(self):
        if self.code != 0:
            raise CommandError(f'({self.cmd}): "{self.output}"')

    @property
    def status(self) -> bool:
        return self.code == 0

    @property
    def output(self) -> 'str | bytes':
        if self.universal_newlines:
            output, end_sign, end_point = '', '\n', -1
        else:
            output, end_sign, end_point = \
                b'', bytes_output_end_sign, bytes_output_end_point

        if self.stdout:
            output += self.stdout
        if self.stderr:
            output += self.stderr

        if output and output[slice(end_point, None)] == end_sign:
            output = output[:end_point]

        return output

    @property
    def code_output(self) -> tuple:
        return self.code, self.output

    @property
    def status_output(self) -> tuple:
        return self.status, self.output

    def output_else_raise(self) -> 'str | bytes':
        self.raise_if_error()
        return self.output

    def output_else_define(self, define=None):
        return self.output if self.status else define

    def contain(self, char: 'str | bytes') -> bool:
        return char in self.output

    def contain_char_else_raise(self, char: 'str | bytes'):
        if char not in self.output:
            raise CommandError(f'({self.cmd}): "{self.output}"')

    def output_if_contain_char_else_raise(
            self, char: 'str | bytes'
    ) -> 'str | bytes':
        output = self.output
        if char in output:
            return output
        raise CommandError(f'({self.cmd}): "{self.output}"')

    def output2dict(self, *, split: str = None):
        result = [
            [value.strip() for value in line.split(split)]
            for line in self.output_else_raise.splitlines()
        ]
        keys = [key.lower() for key in result[0]]
        return (dict(zip(keys, values)) for values in result[1:])


class CommandError(Exception):
    __module__ = 'builtins'


builtins.CommandError = CommandError
