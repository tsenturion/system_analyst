"""экземпляр - конкретный объект созданный на основе класса
атрибут(поле) класса - принадлежит самому классу и разделяется всеми экземплярами
атрибут(поле) экземпляра - принадлежит конкретному объекту  и уникален для каждого экземпляра
метод экземпляра def - функция конкретного объекта с self
метод класса @classmethod- работает с классом в целом. с cls
метод статический @staticmethod- не зависит от класса или объекта, нет доступа, но относится
конструктор __init__- вызывается при создании объекта
наследование - новый класс на основе существующего
полиморфизм - возможность использовать один и тот же интерфейс (метод) для объектов разных классов
инкапсуляция __ - скрытие деталей
свойство - атрибут поволяющий управлять доступом к данным через гет сет дел
дескриптор - объект который оперделяет поведение атрибутов класса __гет__ __сет__ __удалить__
магические методы - __???__ для перегрузки операторов
абстрактный класс - используется как шаблон, указываются методы для реализации
метакласс - определяет поведение других классов
множественное наследование
MRO - порядок поиска методов в иерархии наследования
перегрузка - переопределение поведения операторов и функций
сеттер - устанавливает значение атрибута
геттер - возвращает значение атрибута
делитер - метод удаляет атрибут
приватный атрибут - не предназначен для доступа извне
декораторы - через @
миксины - классы с доп функционалом, не предназначены для самостоятельного использования
"""

class Student:
    is_student = True

    def __init__(self, group_number, course):
        self.group_number = group_number
        self.course = course

    def say_hello(self):
        print('hello ' + self.group_number)

    def checkout():
        print('checkout')

    
print(type("123456789"))
print(len("123456789"))

Matvey = Student('P3212', 2)
print(Matvey.group_number, Matvey.course)

Matvey.course = 3
print(Matvey.group_number, Matvey.course)

John = Student('P3212', 2)

Student.checkout()
print(Student.is_student)
Matvey.say_hello()


class Person:

    health = 100

    def __init__(self, name, age, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student
        self.gender = None

    def invert_is_student(self):
        self.is_student = not self.is_student

    @staticmethod
    def to_learn():
        print('im learning')

    @classmethod
    def print_health(cls):
        print(cls.health)

Person.print_health()
print(Person.health)

num = 1
Matvey = Person('name', 18)
Matvey2 = Person('name', 18)
Matvey2 = Person('name', 18)
print(Matvey.is_student)
Matvey.invert_is_student()
print(Matvey.is_student)
Matvey.to_learn()


"""
создать класс телефон
- поля: марка, модель, цвет, цена
- методы: звонить
"""