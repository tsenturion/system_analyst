import requests

response = requests.get("https://api.github.com")
data = response.json()

print(data["current_user_url"])

if response.status_code == 200:
    print("Тест успешен")
else:
    print("Ошибка:", response.status_code)
