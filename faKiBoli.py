import re

lafz = input("Enter Jumla: ")
if len(lafz) > 0 and lafz.isalpha():
    word = lafz.lower()
    illat = r'(a|e|i|o|u)+'
    subs = r'\1f'
    reg = re.sub(illat,subs,word,0,re.MULTILINE)
    print(reg)
