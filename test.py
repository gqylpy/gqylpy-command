from gqylpy_command import gcmd

ret = gcmd('hostname', timeout=1, ignore_timeout=True).output
print(ret)
