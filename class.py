#CLASS
class MyClass:
    x = 5

#OBJECT
p1 = MyClass()
print(p1.x)

class Waiter:
    def __init__(self):
        self.order = True
        self.serve = True
        self.take = True



Kail = Waiter()
print(Kail.order)


class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

aziz = Person('Aziz', 27) #Object

print(aziz.age)

class Person:
    def __init__(self, n, a):
        self.name = n #attributes
        self.age = a #attributes
    def my_method(self):
     print('The name is',self.name,'and the age is',self.age)

    def order(self):
        print('I have order')



aziz = Person('Aziz', 27) #Object
aziz.order()