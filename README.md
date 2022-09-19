[<img alt="LOGO" src="http://www.gqylpy.com/static/img/favicon.ico" height="21" width="21"/>](http://www.gqylpy.com)
[![Release](https://img.shields.io/github/release/gqylpy/gqylpy-command.svg?style=flat-square")](https://github.com/gqylpy/gqylpy-command/releases/latest)
[![Python Versions](https://img.shields.io/pypi/pyversions/gqylpy_command)](https://pypi.org/project/gqylpy_command)
[![License](https://img.shields.io/pypi/l/gqylpy_command)](https://github.com/gqylpy/gqylpy-command/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/gqylpy_command/month)](https://pepy.tech/project/gqylpy_command)

# gqylpy-command

> 调用系统命令，它是对内置库 subprocess 的二次封装。在 `gcmd` 对象中，提供了多种方法用于判断命令调用结果是否如期。

`pip3 install gqylpy_command`

```python
from gqylpy_command import gcmd

c = gcmd('hostname')

status: bool = c.status
output: str  = c.output
```
