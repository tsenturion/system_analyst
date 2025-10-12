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
class Angry:
    def angry(self):
        print('я злой')

class Good:
    def good(self):
        print('я добрый')
        
class Human(Angry):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Human):
    is_student = True

    def __init__(self, name, age, group_number, course):
        super().__init__(name, age)
        self.group_number = group_number
        self.course = course

    def say_hello(self):
        print('hello ' + self.group_number)

    def checkout():
        print('checkout')

class GoodStudent(Student, Good):
    def __init__(self, name, age, group_number, course):
        super().__init__(name, age, group_number, course)

    def angry(self):
        print("я не злой")
    
Some_student = Student('name', 18, 'P3212', 2)
print(Some_student.name, Some_student.age, Some_student.group_number, Some_student.course)
Some_student.angry()

Good_student = GoodStudent('name', 18, 'P3212', 2)
Good_student.good()
Good_student.angry()

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

class Phone:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    def call(self):
        print('call')


class Animal:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def make_voice(self):
        print(f'{self.name} maked voice')

class Cat(Animal):
    def __init__(self, name, height, weight, color):
        super().__init__(name, height, weight)
        self.color = color

    def greet(self):
        super().make_voice()

cat = Animal('вася', 12, 12)

Cat = Cat('вася', 12, 12, 'black')
Cat.make_voice()
Cat.greet()

# MClass от него унаследовать в тригонометрию
# в триг мат функции
# иниц предыдущее и 1 новое
# из триг вызвать методы MClass


class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(2, 3))
