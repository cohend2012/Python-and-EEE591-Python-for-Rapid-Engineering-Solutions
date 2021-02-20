

import re


str = '### Subject: scuba diving at… From: steve.millman@asu.edu Body: Underwater, where it is at'

# Wan to find : then any char included space but new line , 0 or more, then :
match = re.search(r':.*:',str)
if match:
 print(match.group())
else:
 print('did not find')

# the string st and then one non white space
match = re.search(r'st\S',str)
if match:
 print(match.group())
else:
 print('did not find')
# : then any char include w space not greedy : should be the inner : blah :
match = re.search(r':.*?:', str)
if match:
  print(match.group())
else:
  print('did not find')

# matches one work char, 0 or more, then at, acherored at the end of the str
match = re.search(r'[\w]*at$',str)
if match:
 print(match.group())
else:
 print('did not find')







str = 'blah balh blah <bbbb <tesCode> you rip it ddd> dend <56a> '

#str = 'here is <abcdppppp> and here is another <efgh> and the end'


match = re.search(r'<.*>',str)
if match:
 print(match.group())
else:
 print('did not find')



match = re.search(r'<.*?>',str)
if match:
 print(match.group())
else:
 print('did not find')


str = 'testing blah bMOD347Xalh 85 8 MoD2357x and nowMOD10X the real one MOD10X'

# matches one work char, 0 or more, then at, acherored at the end of the str
match = re.search(r'(?<=MOD)\d+(?=X)',str)
if match:
 print(match.group())
else:
 print('did not find')
