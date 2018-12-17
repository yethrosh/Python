# -*- coding: utf-8  -*-
#!/usr/bin/python
# محمد شعيب
#Utility to modify python2 print functions to be python 3 compatible

import re

with open("py2.py", "r") as f:
    mawad = f.read()
    
reg = r'^print\s+\"(.+)\"+'
sub = r'print("\1")'

tabdil = re.sub(reg,sub, mawad, 0, re.MULTILINE)
with open("py3.py", "w") as f:
    f.write(tabdil)


