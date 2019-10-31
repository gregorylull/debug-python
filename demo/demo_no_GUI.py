"""
n       execute next line
c       complete execution until a breakpoint

l       list 3 lines before and after current line
s       execute the current line and stop at first occasion

u       move the frame up in the stack trace (step up)
d       move the frame down in the stack trace (step down)

p       print, e.g. p(name)
pp      pretty print
h       help
q       quit

source: https://realpython.com/python-debugging-pdb/#essential-pdb-commands

python3 -m pdb demo/demo_no_GUI.py

if you are not using python 3.7+ then:
    1) import pdb
    2) replace 'breakpoint()' with 'pdb.set_trace()'
"""

name = 'greg'

def change_name():
    # breakpoint()
    name = 'lull'
    print('inside', name)

change_name()

print('outside', name)
