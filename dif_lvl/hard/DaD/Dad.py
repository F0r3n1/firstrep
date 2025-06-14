from Character import *


player_name = input("Enter your name: ")
choice = input("Выберите класс игрока (1 – Воин, 2 – Маг): ")


if choice == "1":
    hero = Character.createWarrior(player_name)
elif choice == "2":
    hero = Character.createMage(player_name)
else:
    print("Unknown class. Defaulting to Warrior.")
    hero = Character.createWarrior(player_name)
Character.showInfo