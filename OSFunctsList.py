import os

cur = dir(os)
count = 0
for i in cur:
    count += 1
    print("{0}: {1}".format(count,i))


#Using enumerate 
cur = dir(os)
for i, f in enumerate(cur):
    print("%d: %s" % (i + 1,f))
