#!/usr/bin/python
# محمد شعيب
# Utility to convert # sing in serial numbes in wikitables

with open('wikitable.txt', 'r') as f:
    lines = f.readlines()

newlines = []
line_num = 1

for line in lines:
    newlines.append(line.replace("#",str(line_num)).replace(u"number", u"شمار").replace(u"serial_number",u"شمار"))
    if '#' in line:
        line_num += 1
newlines_str = '\n'.join(line for line in newlines)
    
with open("wikijadwal[trmimshuda].txt", 'w') as f:
            f.write(newlines_str)
