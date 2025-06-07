"""user = {}

def test_first():
    user['first'] = 'john'


def test_last():
    assert user['last'] == 'smith'
"""

"""def test_something():
    if (something):
        # 1 способ
        # проверка
    else:
        # 2 способ
        # проверка
    # проверка
"""

import pytest

@pytest.fixture
def result():
    return sum([5, 9])

def test_sum(result):
    assert result == 14

def test_create_user():
    user = {'name': 'John', 'age': 30}
    assert user['age'] == 30

def test_create_user2():
    user = {'name': 'John', 'age': 30}
    assert user['name'] == 'John'

"""def test_exception():
    try:
        funcion_with_exception(0)
    except Exception as e:
        assert e"""

#import pytest
from pathlib import Path

@pytest.fixture()
def sample_file():
    file_path = Path("test_data.txt")
    file_path.write_text("Hello, World!")

    yield file_path

    file_path.unlink()

def test_read_file(sample_file):
    assert sample_file.read_text() == "Hello, World!"

"""def register_user(**params):
    user = User(**params)
    user.save()
    if os.environ['PROJECT_ENV'] != 'test':
        send_email("registration", user)
    return user.id"""


"""def test_extract_links():
    with_links_path = 'test_data/withLinks.html'
    with open(with_links_path, 'r', encoding='utf-8') as file:
        html = file.read()
        links = extract_links(html)
        assert len(links) == 2
"""