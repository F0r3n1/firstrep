import random
number = random.randint(0,10000)
while True:
    user_input=int(input("Введите догадку: "))
    if user_input < number:
        print("Ваша догадка меньше нужного числа")
    elif user_input>number:
        print("Ваша догадка больше нужного числа")
    else:
        print("Вы угадали число!")
        break
    