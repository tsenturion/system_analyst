# repeat('$', 3)  # '$$$'


def repeat(string, num):
    return string * num

def test_repeat():
    assert repeat('$', 3) == '$$$'