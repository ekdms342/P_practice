Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> letter = 'abcdefghijklmnopqrstuvwxyz'
>>> letter[70:71]
''
>>> len(letter)
26
>>> empty = ""
>>> len(empty)
0
>>> 1*60**2
3600
>>> seconds_per_hour = 1*60**2
>>> seconds_per_hour * 24
86400
>>> second_per_day = seconds_per_hour * 24
>>> second_per_day / second_per_hour
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    second_per_day / second_per_hour
NameError: name 'second_per_hour' is not defined
>>> second_per_day / saconds_per_hour
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    second_per_day / saconds_per_hour
NameError: name 'saconds_per_hour' is not defined
>>> second_per_day /seconds_per_hour
24.0
>>> second_per_day // seconds_per_hour
24
>>> 
