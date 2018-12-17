#!/usr/bin/python
# محمد شعيب

import re

with open('wikitable.txt', 'r') as f:
    lines = f.read()
    
reg = r"^\|(\d+)"
subs = r"|#||\1"
match = re.search(reg, lines)
if match:
    tabdil = re.sub(reg,subs, lines, 0, re.MULTILINE)
    with open("wikitablen.txt", "w") as f:
        f.write(tabdil)
else:    
    newlines =[]
    line_num=1

    for line in lines:
        newlines.append(line.replace("#",str(line_num)))
        if '#' in line:
            line_num += 1
    newlines_str='\n'.join(line for line in newlines)
    
    with open("wikijadwal[trmimshuda].txt", 'w') as f:
            f.write(newlines_str)
