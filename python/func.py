"""
print()
input()
int()
str()
type()
sum()
hash()
sorted()

func
function
static
def
fn
fun

def название функции(аргументы):
может принимать или не принимать аргументы
с аргументами работаем как с переменными
с отступом тело функции
функция может возвращать значение, return
функция может не возвращать значение
"""

def add(a, b):
    print(a + b)

add(3, 3)
print(3 + 3)

print()

print(sum([1, 2, 3, 4, 5]))
print(1)
#number = int(input("Введите число: "))


def do_something():
    print()
    print()


do_something()

def add(a, b):
    """
    Складывает два числа.

    Args:
        a (int): Первое число.
        b (int): Второе число.

    Returns:
        int: Результат сложения.

    Raises:
        TypeError: Если аргументы не являются числами.
    """
    return a + b

print(add(3, 3))




def print_even(n):
    """
    Prints even numbers from 0 to n, excluding multiples of 3.
    
    Parameters:
        n (int): The upper limit of the range of numbers to print.
        
    Returns:
        None
    """
    for i in range(n):
        if i % 2 == 0:
            if i % 3 == 0:
                print(i)
            else:
                print(i)

n = int(input("Введите число: "))
print_even(n)

"""
создайте функцию, которая принимает на вход 2 аргумента
проверить, что аргументы - числа
если аргументы - числа, то сложить их
если аргументы не числа, то показать типы данных

для первого аргумента:
    если тип данных - int, то вывести все числа от 0 до аргумента
"""