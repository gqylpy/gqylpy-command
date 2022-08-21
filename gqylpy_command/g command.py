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
from subprocess import check_output, TimeoutExpired, CalledProcessError

import gqylpy_cache


class GqylpyCommand(metaclass=gqylpy_cache):
    code = 0

    def __init__(
            self,
            cmd: str,
            *,
            timeout: int = None,
            ignore_timeout_error: bool = False,
            **kw
    ):
        try:
            self.raw_output: str = check_output(
                cmd,
                timeout=timeout,
                shell=True,
                text=True,
                stderr=-2,
                **kw
            )
        except CalledProcessError as e:
            self.raw_output: str = e.output
            self.code: int = e.returncode
        except TimeoutExpired as e:
            if not ignore_timeout_error:
                raise e
            self.raw_output = ''
            self.code = 1
        self.cmd = cmd

    def raise_if_error(self):
        if self.code != 0:
            raise CommandError(f'({self.cmd}) {self.output}')

    @property
    def status(self) -> bool:
        return self.code == 0

    @property
    def output(self) -> str:
        if self.raw_output[-1:] == '\n':
            return self.raw_output[:-1]
        return self.raw_output

    @property
    def code_output(self) -> tuple:
        return self.code, self.output

    @property
    def status_output(self) -> tuple:
        return self.status, self.output

    @property
    def output_else_raise(self) -> str:
        if self.status:
            return self.output
        raise CommandError(f'({self.cmd}) {self.output}')

    def output_else_define(self, define=None):
        return self.output if self.status else define

    def contain_string(self, string: str) -> bool:
        return string in self.raw_output

    def output_if_contain_string_else_raise(self, string: str) -> str:
        if self.contain_string(string):
            return self.output
        raise CommandError(f'({self.cmd}): "{self.output}"')

    def table_output_to_dict(self, split: str = None) -> list:
        result = [
            [value.strip() for value in line.split(split)]
            for line in self.output_else_raise.splitlines()
        ]
        keys = [key.lower() for key in result[0]]
        return [dict(zip(keys, values)) for values in result[1:]]


class CommandError(Exception):
    __module__ = 'builtins'
