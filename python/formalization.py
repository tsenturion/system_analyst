"""
Разбиение задачи на логические шаги.
Определение входных и выходных данных.
Построение схемы алгоритма (псевдокод, блок-схемы, диаграммы).
Реализация алгоритма на языке программирования.
Тестирование и верификация корректности работы.

Задача: Найти среднее значение чисел в списке.
"""

# Список чисел
numbers = [10, 20, 30, 40, 50]

# 1. Сумма всех чисел
total = sum(numbers)

# 2. Количество элементов
count = len(numbers)

# 3. Среднее значение
average = total / count

# 4. Вывод результата
print("Среднее значение:", average)

def calculate_average(numbers):
    """Функция для вычисления среднего значения списка"""
    total = sum(numbers)
    count = len(numbers)
    return total / count

# Использование функции
numbers = [5, 15, 25]
result = calculate_average(numbers)
print("Среднее значение:", result)

def check_number_type(number):
    if number > 0:
        return "Положительное"
    elif number < 0:
        return "Отрицательное"
    else:
        return "Ноль"

print(check_number_type(10))
print(check_number_type(-5))
print(check_number_type(0))

numbers = [2, 4, 6, 8]

# Цикл for
for number in numbers:
    print(number)

# Цикл while
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

import csv

numbers = []

with open("data.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        numbers.append(int(row['value']))

average = sum(numbers) / len(numbers)
print("Среднее значение из CSV:", average)

def safe_average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0  # если список пустой

print(safe_average([10, 20]))
print(safe_average([]))

numbers = [1, 2, 2, 3, 3, 3]
unique_numbers = set(numbers)
print("Уникальные значения:", unique_numbers)

"""
Вам поступают ежедневные данные о транзакциях компании. 
В выгрузке могут встречаться некорректные данные — пустые значения или строки вместо чисел. 
Необходимо разработать алгоритм, который позволит корректно обработать такие данные и вычислить итоговую статистику.
Задача
Считать данные о транзакциях из списка.
Отфильтровать некорректные значения (оставить только числа).
Вычислить:
общую сумму всех корректных транзакций;
количество корректных транзакций;
среднее значение корректных транзакций.

Если корректных данных нет — среднее значение должно быть равно 0.

Данные для работы
transactions = [120, '', 300, 'ошибка', 90, 200, '']

Требования
Сначала опишите алгоритм в виде пошагового описания или псевдокода.
Продумайте, как обрабатывать некорректные данные без аварийного завершения программы.
"""
