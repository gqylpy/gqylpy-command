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
__version__ = 1, 0, 'alpha2'
__author__ = '竹永康 <gqylpy@outlook.com>'
__source__ = 'https://github.com/gqylpy/gqylpy-datastruct'


class GqylpyCommand:
    """
    Executes the incoming command directly at instantiation time.
    """
    code: int  # Command exit code.
    raw_output: str  # Command output.

    def __init__(
            self,
            cmd: str,
            *,
            timeout: int = None,
            ignore_timeout_error: bool = False
    ):
        """
        @param cmd:                  Command string.
        @param timeout:              Command timeout, Default never times out.
        @param ignore_timeout_error: If true, no exception is thrown after naming timeout.
        """

    def raise_if_error(self):
        if self.code != 0:
            raise CommandError

    @property
    def status(self) -> bool:
        return self.code == 0

    @property
    def output(self) -> str:
        return process(self.raw_output)

    @property
    def code_output(self) -> 'Tuple[int, str]':
        return self.code, self.output

    @property
    def status_output(self) -> 'Tuple[bool, str]':
        return self.status, self.output

    @property
    def output_else_raise(self) -> str:
        if self.status:
            return self.output
        raise CommandError

    def output_else_define(self, define: 'Any' = None) -> 'Any':
        return self.output if self.status else define

    def contain_string(self, string: str) -> bool:
        return string in self.raw_output

    def output_if_contain_string_else_raise(self, string: str) -> str:
        if self.contain_string(string):
            return self.output
        raise CommandError

    def table_output_to_dict(self, split: str = None) -> list:
        return table2dict(self.output_else_raise, split=split)


def table2dict(table: str, *, split: str = None) -> list:
    """Used to turn the command output result with a title
    into a dictionary, such as `kubectl get nodes`."""


class _______G________Q________Y_______L_______P_______Y_______:
    import sys

    __import__(f'{__name__}.g {__name__[7:]}')
    gpack = sys.modules[__name__]
    gcode = globals()[f'g {__name__[7:]}']

    for gname in globals():
        if gname[0] != '_' and hasattr(gcode, gname):
            setattr(gpack, gname, getattr(gcode, gname))


gcmd = GqylpyCommand

from typing import Any, Tuple
