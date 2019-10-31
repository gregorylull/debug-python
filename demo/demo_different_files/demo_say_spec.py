import demo_say as demo

def say_spec():
    say = demo.say

    default_case = 'hi'
    name = 'greg'
    msg = 'bye'

    # common cases
    assert say() == default_case
    assert say(name, msg) == 'hi greg, bye'
    assert say(name) == 'hi greg'
    assert say('', msg) == 'hi, bye'

    # corner cases
    assert say(5, {}) == default_case

    assert say(name, 5) == default_case
    assert say(5, msg) == default_case

    assert say(name, {}) == default_case
    assert say({}, msg) == default_case


if __name__ == '__main__':
    say_spec()