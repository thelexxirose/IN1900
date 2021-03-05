class Mammal:
    def __init__(self):
        pass

    def info(self):
        return "I have hair on my body."

    def identify_mammal(self):
        print("I am a mammal")


class Primate(Mammal):

    def info(self):
        return super().info() + " I have a large brain."

    def identify_primate(self):
        print("I am a primate")


class Human(Primate):

    def info(self):
        return super().info() + " I can speak."

    def identify_human(self):
        print("I am a human")


class Ape(Primate):

    def info(self):
        return super().info() + " I can create some simple tools."

    def identify_ape(self):
        print("I am an ape")


John = Human()
Julius = Ape()

print(John.info())
John.identify_mammal()
John.identify_primate()
John.identify_human()
# The method identify_ape() does not exist for John, since he is a human, and will therefore raise an error
# John.identify_ape()

print("\n")

print(Julius.info())
Julius.identify_mammal()
Julius.identify_primate()
# The method identify_human() does not exist for Julius, since he is an ape, and will therefore raise an error
# Julius.identify_human()
Julius.identify_ape()

print("\n")

print(f"John is a Mammal = {isinstance(John, Mammal)}")
print(f"John is a Primate = {isinstance(John, Primate)}")
print(f"John is a Human = {isinstance(John, Human)}")
print(f"John is a Ape = {isinstance(John, Ape)}")

print("\n")

print(f"Julius is a Mammal = {isinstance(Julius, Mammal)}")
print(f"Julius is a Primate = {isinstance(Julius, Primate)}")
print(f"Julius is a Human = {isinstance(Julius, Human)}")
print(f"Julius is a Ape = {isinstance(Julius, Ape)}")

'''
(base) corybalaton@Corys-MacBook-Pro Uke 44 % /Users/corybalaton/opt/anaconda3/bin/python "/Users/corybalaton/Documents/UiO/IN1900/Uke 44/inheritance.py"
I have hair on my body. I have a large brain. I can speak.
I am a mammal
I am a primate
I am a human


I have hair on my body. I have a large brain. I can create some simple tools.
I am a mammal
I am a primate
I am an ape


John is a Mammal = True
John is a Primate = True
John is a Human = True
John is a Ape = False


Julius is a Mammal = True
Julius is a Primate = True
Julius is a Human = False
Julius is a Ape = True
'''
