import demo_say_hello as demo

def say_hello_spec():
    say_hello = demo.say_hello
    default_case = 'hi'
    name = 'greg'
    phrase = 'bye'

    # common cases
    assert say_hello() == default_case
    assert say_hello(name, phrase) == 'hi greg, bye'
    assert say_hello(name) == 'hi greg'
    assert say_hello(None, phrase) == 'hi, bye'

    # corner cases
    assert say_hello(5, phrase) == default_case
    assert say_hello(5, {}) == default_case
    assert say_hello(name, {}) == default_case

if __name__ == '__main__':
    say_hello_spec()