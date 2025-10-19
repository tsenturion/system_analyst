# pip install pytest
# pip install flake8
from add_func import add


def test_add_positive() -> None:
    assert add(2, 3) == 5


def test_add_zero() -> None:
    assert add(0, 0) == 0
    assert add(1, 0) == 1
    assert add(0, 1) == 1


def test_add_negative() -> None:
    assert add(1, -1) == 0
    assert add(-1, -1) == -2


print("тест прошел")
