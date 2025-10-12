def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b

# Тест
try:
    assert divide(10, 2) == 5
    print("Тест 1 пройден")
except AssertionError:
    print("Ошибка: неверный результат")

def test_login_api():
    """Проверка, что API авторизации возвращает код 200"""
    response = requests.post("https://example.com/login", data={"user": "admin", "password": "123"})
    assert response.status_code == 200
