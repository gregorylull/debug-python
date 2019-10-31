# takes a name and a msg,
#   1) if either is valid and not empty then return a message f'hi {name}, {msg}'
#   2) if either is invalid or empty then return a default 'hi'
# 
# examples
#     say() --> 'hi' 
#     say('greg', 'bye') --> 'hi greg, bye'
#     say('greg') --> 'hi greg'
#     say('', 'bye') --> 'hi, bye'
#     say(5, {}) --> 'hi'
def say(name='', msg=''):

    name_not_valid = name and type(name) != str
    phrase_not_valid = msg and type(msg) != str
    
    if name_not_valid or phrase_not_valid: 
        message = 'hi'

    elif name and msg:
        message = f'hi {name}, {msg}'      
    
    elif name:
        message = f'hi {name}'
    
    elif msg:
        message = f'hi, {msg}'
    
    else:
        message = 'hi'



