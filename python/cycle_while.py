count = 0
while count < 10:
    print(count)
    count += 1
else:
    print("цикл завершен")

my_input = input()
while my_input != "выход":
    print("Вы ввели:", my_input)
    my_input = input()

count = 0
while 6 < 4:
    print(count)
    count += 1

"""
while - цикл пока, с условием
break - полностью прерывает цикл
continue - пропускает итерацию
"""

count = 0
while True:
    if count == 10:
        break

    if count % 2 == 0:
        count += 1
        continue
        
    print(count)
    count += 1
else:
    print("цикл завершен")

"""

пока вводится число:
    печатать его, если оно четное
    пропускать, если нечетное
    если вводится 0, то выйти из цикла
    если ввводится не число, то вывести сообщение и выйти из цикла
"""
data = input()
while data != '0':
    if int(data) % 2 == 0:
        print("вы ввели четное число: ", data)
    data = input()

while data := input() != '0':
    try:
        data = int(data)
    except Exception:
        print('вы ввели не число')
        break

    if data % 2 == 0:
        print("вы ввели четное число: ", data)

while data := input() != '0':
    if data.isdigit():
        if int(data) % 2 == 0:
            print("вы ввели четное число: ", data)
    else:
        print('вы ввели не число')
        break


try:
    x = int("abc")  # Ошибка преобразования
except ValueError as e:
    print("Тест упал с ошибкой:", e)
