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
__version__ = 1, 0, 'alpha3'
__author__ = '竹永康 <gqylpy@outlook.com>'
__source__ = 'https://github.com/gqylpy/gqylpy-command'


class GqylpyCommand:
    PIPE, STDOUT, DEVNULL = -1, -2, -3

    def __init__(
            self,
            *cmdline,

            stdin:  'Optional[int]' = None,
            stdout: 'Optional[int]' = None,
            stderr: 'Optional[int]' = None,

            shell:   bool = None,
            cwd:     str  = None,
            env:     dict = None,
            bufsize: int  = None,

            text:               bool = None,
            universal_newlines: bool = None,

            input:          'Union[bytes, str]' = None,
            timeout:         float              = None,
            ignore_timeout:  bool               = None,

            **other_hardly_used_params
    ):
        self.cmd:    str                     = ''.join(cmdline)
        self.code:   int                     = ...
        self.stdout: Union[bytes, str, None] = ...
        self.stderr: Union[bytes, str, None] = ...

    def raise_if_error(self) -> 'NoReturn':
        if self.code != 0:
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

    @property
    def output_else_raise(self) -> 'Union[bytes, str]':
        """Return output if the command
        exitcode is 0 else raise CommandError.
        """
        self.raise_if_error()
        return self.output

    def output_else_define(self, define: 'Any' = None) -> 'Any':
        return self.output if self.status else define

    def contain(self, char: 'Union[bytes, str]') -> bool:
        return char in self.output

    def contain_char_else_raise(self, char: 'Union[bytes, str]') -> 'NoReturn':
        if char not in self.output:
            raise CommandError

    def output_if_contain_char_else_raise(self, char: 'Union[bytes, str]') -> 'str | bytes':
        if self.contain(char):
            return self.output
        raise CommandError

    def table_output_to_dict(self, split: str = None) -> list:
        """Used to turn the command output result with a title
        into a dictionary, such as `kubectl get nodes`."""


class _xe6_xad_x8c_xe7_x90_xaa_xe6_x80_xa1_xe7_x8e_xb2_xe8_x90_x8d_xe4_xba_x91:
    __import__(f'{__name__}.g {__name__[7:]}')
    globals()['GqylpyCommand'] = globals()[f'g {__name__[7:]}'].GqylpyCommand


gcmd = GqylpyCommand

from typing import Any, Tuple, Union, Optional, NoReturn
