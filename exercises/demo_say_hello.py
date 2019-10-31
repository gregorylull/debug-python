# say_hello() --> 'hi' 
# say_hello('greg', 'bye') --> 'hi greg, bye'
# say_hello('greg') --> 'hi greg'
# say_hello(None, 'bye') --> 'hi, bye'
# say_hello(5, {}) --> 'hi'
def say_hello(name='', phrase=''):

    if (name and type(name) != str) or (phrase and type(phrase) != str): 
       return 'hi'

    if name and phrase:
        return f'hi {name}, {phrase}'      
    
    elif name:
        return f'hi {name}'
    
    elif phrase:
        return f'hi, {phrase}'
    
    else:
        return 'hi'


