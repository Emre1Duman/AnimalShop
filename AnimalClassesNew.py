#from abc import ABC, abstractmethod

class Animals:
    def __init__(self, name, type, eat, price):
        self.name = name
        self.type = type
        self.eat = eat
        self.price = price
        
    def introduce_self(self):
        return("My name is " + self.name +", "+ "I am a " + self.type +", "+ "I eat " + self.eat)
    
    def animal_Price(self):
        return("Buy me for", self.price)

    def animal_type(self):
        return(self.type)
     
#objects
Cat = Animals("Jerry", "Cat", "Mice", 100)
Bat = Animals("Batty", "Bat", "Insects", 69)
Dog = Animals("Doggy", "Dog", "Cats", 101)
Penguin = Animals("Pengu", "Penguin", "Fish", 404)
Pigeon = Animals("Pigi", "Pigeon", "Crumbs", 2)
Goldfish = Animals("Goldi", "GoldFish", "Plants", 5)
Hamster = Animals("Hammy", "Hamster", "Fruits", 30)



'''
print(Cat.introduce_self())
print(Cat.animal_Price())

print(Bat.introduce_self())
print(Bat.animal_Price())

print(Dog.introduce_self())
print(Dog.animal_Price())

print(Penguin.introduce_self())
print(Penguin.animal_Price())

print(Pigeon.introduce_self())
print(Pigeon.animal_Price())

print(Goldfish.introduce_self())
print(Goldfish.animal_Price())

print(Hamster.introduce_self())
print(Hamster.animal_Price())
'''
    
