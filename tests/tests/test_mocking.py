"""@pook.on
def test_get_private_fork_names():
    mock = pook.get(
        "https://api.github.com/users/tsenturion/repos",
        reply=200,
        response_json=['fork': true, 'name': 'one'], {'fork': false, 'name': 'two'}
    )

    get_private_fork_names('tsenturion')
    assert mock.calls == 1
"""


def for_each(coll, callback):
    for c in coll:
        callback(c)


for_each([1, 2, 3], lambda c: print(c))

from unittest.mock import Mock

def test_for_each():
    mock = Mock()
    for_each([1, 2, 3], lambda c: mock(c))
    assert mock.call_count == 3
    mock.assert_any_call(1)
    mock.assert_any_call(2)
    mock.assert_any_call(3)

def test_for_each2():
    result = []
    numbers = [1, 2, 3]
    for_each(numbers, lambda c: result.append(c))
    assert result == numbers

class MyObject:
    def __init__(self, dependency):
        self.dependency = dependency

    def my_method(self, arg):
        return self.dependency.do_something(arg)

def test_my_method():
    mock_dependency = Mock()
    my_object = MyObject(mock_dependency)
    mock_dependency.do_something.return_value = "mocked value"
    result = my_object.my_method("test")
    mock_dependency.do_something.assert_called_once_with("test")
    assert result == "mocked value"

"""thing = ProductionClass()
thing.method = Mock(return_value='mocked value')
thing.method('foo')
thing.method.assert_called_once_with('foo')"""