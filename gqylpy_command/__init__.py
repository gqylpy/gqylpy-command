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

Copyright © 2022 GQYLPY. 竹永康 <gqylpy@outlook.com>

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
__version__ = 1, 0, 'dev1'


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
            ignore_timeout: bool = False
    ):
        """
        @param cmd:            Command string.
        @param timeout:        Command timeout, Default never times out.
        @param ignore_timeout: If true, no exception is thrown after naming timeout.
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


def raise_if_error(cmd: str, *, timeout: int = None):
    GqylpyCommand(cmd, timeout=timeout).raise_if_error()


def code(cmd: str, *, timeout: int = None) -> int:
    return GqylpyCommand(cmd, timeout=timeout).code


def status(cmd: str, *, timeout: int = None) -> bool:
    return GqylpyCommand(cmd, timeout=timeout).status


def output(cmd: str, *, timeout: int = None) -> str:
    return GqylpyCommand(cmd, timeout=timeout).output


def raw_output(cmd: str, *, timeout: int = None) -> str:
    return GqylpyCommand(cmd, timeout=timeout).raw_output


def code_output(cmd: str, *, timeout: int = None) -> 'Tuple[int, str]':
    return GqylpyCommand(cmd, timeout=timeout).code_output


def status_output(cmd: str, *, timeout: int = None) -> 'Tuple[bool, str]':
    return GqylpyCommand(cmd, timeout=timeout).status_output


def output_else_raise(cmd: str, *, timeout: int = None) -> str:
    return GqylpyCommand(cmd, timeout=timeout).output_else_raise


def output_else_define(
        cmd: str,
        *,
        define: 'Any' = None,
        timeout: int = None
) -> 'Any':
    return GqylpyCommand(
        cmd, timeout=timeout
    ).output_else_define(define)


def contain_string(
        cmd: str,
        *,
        string: str = None,
        timeout: int = None
) -> bool:
    return GqylpyCommand(
        cmd, timeout=timeout
    ).contain_string(string)


def output_if_contain_string_else_raise(
        cmd: str,
        *,
        string: str = None,
        timeout: int = None
) -> str:
    return GqylpyCommand(
        cmd, timeout=timeout
    ).output_if_contain_string_else_raise(string)


def table_output_to_dict(cmd: str, *, timeout: int = None) -> list:
    return GqylpyCommand(cmd, timeout=timeout).table_output_to_dict()


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
