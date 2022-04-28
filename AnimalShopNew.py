from AnimalClassesNew import *

menu = input("Welcome to the Pet Shop, select an option, Browse Stock(a), Quit(b)")

# See animals, select animal for more info, buy animal
if menu == "a":
    print(Cat.animal_type())
    print(Bat.animal_type())
    print(Dog.animal_type())
    print(Penguin.animal_type())
    print(Pigeon.animal_type())
    print(Goldfish.animal_type())
    print(Hamster.animal_type())
    message = input(" Select animal for more detail [Make sure its lowercase :) ]: ")   
    if message == "cat":
        print(Cat.introduce_self())
        print(Cat.animal_Price())
    elif message == "bat":
        print(Bat.introduce_self())
        print(Bat.animal_Price())
    elif message == "dog":
        print(Dog.introduce_self())
        print(Dog.animal_Price())
    elif message == "penguin":
        print(Penguin.introduce_self())
        print(Penguin.animal_Price())
    elif message == "pigeon":
        print(Pigeon.introduce_self())
        print(Pigeon.animal_Price())
    elif message == "goldfish":
        print(Goldfish.introduce_self())
        print(Goldfish.animal_Price())
    elif message == "hamster":
        print(Hamster.introduce_self())
        print(Hamster.animal_Price())               
    else:
        print("bye")





'''
if menu =="b":
    import sys
    sys.exit()
'''

 