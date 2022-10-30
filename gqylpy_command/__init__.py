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
__version__ = 1, 1
__author__ = '竹永康 <gqylpy@outlook.com>'
__source__ = 'https://github.com/gqylpy/gqylpy-command'


class GqylpyCommand:
    PIPE, STDOUT, DEVNULL = -1, -2, -3

    def __init__(
            self,
            *cmdline,

            stdin:  'Union[int, None]' = PIPE,
            stdout: 'Union[int, None]' = PIPE,
            stderr: 'Union[int, None]' = PIPE,

            shell:   bool = None,
            cwd:     str  = None,
            env:     dict = None,
            bufsize: int  = None,

            text:               bool = None,
            universal_newlines: bool = None,

            input:          'Union[bytes, str]' = None,
            timeout:        'Union[int, float]' = None,
            ignore_timeout:  bool               = None,

            **other_hardly_used_params
    ):
        """
        @param *cmdline: A command string, or a sequence of program arguments.

        @param stdin:  Standard input, default point to PIPE(-1).
        @param stdout: Standard output, default point to PIPE(-1). If you want
                       to output the result of the command directly to terminal
                       specify to None. If the output is not needed, specify to
                       DEVNULL(-3).
        @param stderr: Standard error output, default point to PIPE(-1). If you
                       want to output the error result of the command directly
                       to terminal specify to None. If you want to redirect the
                       standard error output to standard output specify to
                       STDOUT(-2). If the output is not needed, specify to
                       DEVNULL(-3).

        @param shell:   Execute the command through shell, default True.
        @param cwd:     In which path to execute the command, default is the
                        path of the current Python process.
        @param env:     Define the ENV, can be used in the command. Indication:
                        system may reject environment variables.
        @param bufsize: Supplied as the parameter "buffering" to the `io.open()`
                        function when creating the stdin/stdout/stderr pipe file
                        object.

        @param text:               If True, the output type is string, otherwise
                                   bytes.
        @param universal_newlines: Same as parameter "text", this parameter is
                                   provided for backward compatibility. use
                                   parameter "text" is recommended.

        @param input:          Data sent to the child process executing the
                               command, default no data is send. If the
                               parameter "text" is True, the type of data to be
                               sent must be string, otherwise bytes.
        @param timeout:        Duration of waiting for the child process to
                               execute the command (in seconds), default
                               permanent. Terminate the child process after the
                               timeout and raise exception "TimeoutExpired".
        @param ignore_timeout: Used to ignore exception raised because of
                               timeout, used with the parameter "timeout". If
                               True, terminate the child process after the
                               timeout but not raise exception, default False.

        @param **other_hardly_used_params: Other hardly used parameters, based
                                           on "subprocess.Popen".
        """
        self.cmd:    str                     = ''.join(cmdline)
        self.code:   int                     = ...  # command exitcode
        self.stdout: Union[bytes, str, None] = ...  # command output
        self.stderr: Union[bytes, str, None] = ...  # command error output

    def raise_if_error(self) -> 'NoReturn':
        if not self.status:
            raise CommandError

    @property
    def status(self) -> bool:
        return self.code == 0

    @property
    def output(self) -> 'Union[bytes, str]':
        return self.stdout + self.stderr

    @property
    def code_output(self) -> 'Tuple[int, str]':
        return self.code, self.output

    @property
    def status_output(self) -> 'Tuple[bool, str]':
        return self.status, self.output

    def output_else_raise(self) -> 'Union[bytes, str]':
        self.raise_if_error()
        return self.output

    def output_else_define(self, define: 'Optional[Any]' = None) -> 'Any':
        return self.output if self.status else define

    def contain(self, char: 'Union[bytes, str]') -> bool:
        return char in self.output

    def contain_char_else_raise(self, char: 'Union[bytes, str]') -> 'NoReturn':
        if not self.contain(char):
            raise CommandError

    def output_if_contain_char_else_raise(
            self, char: 'Union[bytes, str]'
    ) -> 'str | bytes':
        if self.contain(char):
            return self.output
        raise CommandError

    def output2dict(self, split: 'Optional[str]' = None) -> 'Generator':
        """Used to turn the command output result with a title
        into a dictionary, such as `kubectl get nodes`."""


PIPE, STDOUT, DEVNULL = -1, -2, -3


class _xe6_xad_x8c_xe7_x90_xaa_xe6_x80_xa1_xe7_x8e_xb2_xe8_x90_x8d_xe4_xba_x91:
    __import__(f'{__name__}.g {__name__[7:]}')
    globals()['GqylpyCommand'] = globals()[f'g {__name__[7:]}'].GqylpyCommand


gcmd = GqylpyCommand

from typing import Any, Tuple, Union, NoReturn, Generator, Optional
