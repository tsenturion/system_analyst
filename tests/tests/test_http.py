import requests
import pytest

def get_fork_names(owner: str, repo: str, token: str) -> list:
    url = f"https://api.github.com/repos/{owner}/{repo}/forks"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    fork_names = []
    page = 1

    while True:
        response = requests.get(url, headers=headers, params={"page": page, "per_page": 100})

        if response.status_code != 200:
            raise Exception(f"Ошибка запроса: {response.status_code} — {response.text}")

        forks = response.json()
        if not forks:
            break

        fork_names.extend([fork["full_name"] for fork in forks])
        page += 1

    return fork_names


owner = 'tsenturion'
repo = 'top-python'

"""forks = get_fork_names(owner, repo, token)
print(forks)"""

"""def test_get_private_fork_names():
    names = get_fork_names(owner, repo, token)
    assert 'Appxkk/top-python' in names"""

def get_private_fork_names_2(username, client):
    repos = client.get_user(username).get_repos(type='private')
    return [repo.name for repo in repos if repo.fork]

class GithubFake:
    def __init__(self, data):
        self.data = data

    def get_user(self, name):
        return self

    def get_repos(self, type):
        return self.data

#from github_fake import GithubFake

def test_get_private_fork_names():
    class FakeRepo:
        def __init__(self, name, fork):
            self.name = name
            self.fork = fork

    test_data = [
        FakeRepo('repo1', True),
        FakeRepo('repo2', False),
        FakeRepo('repo3', True),
    ]

    client = GithubFake(test_data)
    names = get_private_fork_names_2('username', client)
    assert names == ['repo1', 'repo3']

from github import Github

def get_private_fork_names(username):
    client = Github(token)
    repos = client.get_user(username).get_repos(type='private')
    return [repo.name for repo in repos if repo.fork]

def test_get_private_fork_names2(monkeypatch):
    def fake_get_repos(self, *args, **kwargs):
        return [
            type('Repo', (), {'name': 'repo1', 'fork': True})(),
            type('Repo', (), {'name': 'repo2', 'fork': False})(),
            type('Repo', (), {'name': 'repo3', 'fork': True})(),
        ]

    monkeypatch.setattr(Github, 'get_user', lambda self, username: self)
    monkeypatch.setattr(Github, 'get_repos', fake_get_repos)

    result = get_private_fork_names('username')
    assert result == ['repo1', 'repo3']

"""import pook
# import requests

@pook.on
def test_my_api():
    pook.get(
        'http://twitter.com/api/1/footbar',
        reply=404,
        response_json={'error': 'Not found'},
    )

    response = requests.get('http://twitter.com/api/1/footbar')
    assert response.status_code == 404
    assert response.json() == {'error': 'Not found'}"""

"""import pook
# import requests

@pook.on
def test_get_private_fork_names():
    pook.get(
        'http://github.com/orgs/tsenturion/repos/',
        reply=200,
        response_json=[
                {'name': 'one', 'fork': True},
                {'name': 'two', 'fork': False},
            ]
    )

    names = get_private_fork_names('tsenturion')
    assert names == ['one']
"""

@pytest.mark.vcr
def test_get_private_fork_names():
    assert get_private_fork_names('tsenturion') == ['one']
"""class EmailSender:
    def send(self, message):
        print(f'Отправка email: {message}')


def notify_user(user_id):
    sender = EmailSender()
    sender.send(f'Уведомление для пользователя {user_id}')

def process_order(order_id):
    notify_user(order_id)


def notify_user2(user_id, sender=EmailSender()):
    sender.send(f'Уведомление для пользователя {user_id}')

def process_order2(order_id, sender):
    notify_user2(order_id, sender)

class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

user = User('John Doe')
user.get_name()

patch_name = lambda : 'Alice'
user.get_name = patch_name

user.get_name()"""


