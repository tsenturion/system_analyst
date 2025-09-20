"""

пока вводится число:
    печатать его, если оно четное
    пропускать, если нечетное
    если вводится 0, то выйти из цикла
"""
data = input()
while data != '0':
    if int(data) % 2 == 0:
        print("вы ввели четное число: ", data)
    data = input()

while data := input() != '0':
    try:
        data = int(data)
    except ValueError:
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