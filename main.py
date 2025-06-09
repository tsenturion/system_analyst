"""
модульные - проверка функций или других конкретных модулей программы
интеграционные - охватывают большую часть системы, проверяют взаимодействие нескольких модулей
системные - проверяют все модули системы, взаимодействие которых нарушается, при изменении одной из них.

python -i main.py
"""
def capitalize(text):
    first_char = text[0].upper()
    rest_substring = text[1:]
    return first_char + rest_substring

capitalize('hello world')

# def название_функции(аргумент1, аргумент2, ..., аргументn):
# def функция():

# 1 с аргументами
def add(a, b):
    print(a + b)

add(3, 2)

# 2 без аргументов
def custom_print_my_print():
    print('hello world')

custom_print_my_print()

# 3 с возвращаемым значением
def add(a, b: int):
    return a + b

result = add(3, 2)
print(result)

"""def add(a, b=None):
    return 1, 2, 3, 4

def add(a, b=None):
    yield 3"""
"""
функции

input("подсказка пользователю")

print()
int()
float()

"""

str1 = 'hello'
# [] =  01234
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])

print(list(range(5)))
print(list(range(0, 5, 1)))
print(list(range(20, 5000, 100)))
print(list(range(20000, 5000, -100)))
print('-' * 20)

str1 = 'hello world'
print(str1[2:9:2])
print(str1[::-1])


print(type("123"))



print('hello' + 'world')


try:
    capitalize('hello world')
except Exception as err:
    print(err)


raise ValueError('ошибка ввода данных')