class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def change_gender(self, gender):
        self.gender = gender

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, gender: {self.gender}"


p1 = Person("John", 55, "Male")

print(p1)

p1.change_name("Jenny")
p1.change_gender("Female")

print(p1)

'''
(base) corybalaton@Corys-MacBook-Pro Uke 43 %
/Users/corybalaton/opt/anaconda3/bin/python
"/Users/corybalaton/Documents/UiO/IN1900/Uke 43/class_people.py"

name: John, age: 55, gender: Male
name: Jenny, age: 55, gender: Female
'''
