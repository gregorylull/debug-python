"""

n       execute next line
c       complete execution
l       list 3 lines before and after current line
s       step into function call

b       show list of all break points
b[int]  set breakpoint at line number (e.g. b10)
b[func] break at function name
cl      clear all breakpoints
cl[int] clear break point at line number (e.g. cl10)
p       print

source: https://www.youtube.com/watch?v=ChuU3NlYRLQ

"""

import pdb

name = 'greg'

pdb.set_trace()

print('name: ', name)

def change_name():
    name = 'lull'

pdb.set_trace()

change_name()

print('name?', name)
