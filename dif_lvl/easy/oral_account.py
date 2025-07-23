from random import randint as ri
from random import choice as ch

def generate_example():
    correct = 0
    wrong = 0
    while correct + wrong < 15:
        operations = ['+', '-', '*']
        num1 = ri(1, 10)
        num2 = ri(1, 10)
        operation = ch(operations)
        
        problem = f"{num1} {operation} {num2}"
        answer = eval(problem)
        
        try:
            user_ans = int(input(f"Решите пример: {problem}. Решение: "))
            if answer == user_ans:
                print("Пример решен правильно!")
                correct += 1
            else:
                print(f"Пример решен неправильно! Правильный ответ: {answer}")
                wrong += 1
        except ValueError:
            print("Пожалуйста, вводите только числа!")
    
    print(f"Вы решили 15 примеров, из них {wrong} неправильные")

generate_example()