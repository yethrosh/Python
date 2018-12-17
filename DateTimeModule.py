# -*- coding: utf-8  -*-
#!/usr/bin/python
# محمد شعيب

from datetime import datetime
import calverter #for hijri calender

#Current date & time
now = datetime.now()
print(now)

#Current formatted date
time12 = now.strftime('%I:%M:%S')
print("{0}/{1}/{2}, and Current time is {3}".format(now.day,now.month,now.year,time12))
#24-hour format
print(now.strftime('%Y/%m/%d %H:%M:%S'))
#12-hour format
print(now.strftime('%Y/%m/%d %I:%M:%S'))

