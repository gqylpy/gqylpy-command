from gqylpy_command import gcmd

c = gcmd('hostname')

c.raise_if_error()

code:   int  = c.code
status: bool = c.status
output: str  = c.output

code,   output = c.code_output
status, output = c.status_output

output: str = c.output_else_raise()
output: str = c.output_else_define(...)

c.contain_char_else_raise('char')
output: str = c.output_if_contain_char_else_raise('char')
