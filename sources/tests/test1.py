import json


with open(r"C:\Users\f0r3n\Desktop\ваэно\pyproject\firstrep\dif_lvl\normal\toDo\toDo.json", "r") as file:
    toDo_list = json.load(file)

print(len(toDo_list))


# test={}
# name = input("name")
# desc=input("desc")
# test[name]=desc


# toDo_list = {}

# # while True:
# #     task = input("Введите задачу (или 'выход' чтобы закончить): ")
# #     if task.lower() == 'выход':
# #         break

# #     description = input("Введите описание задачи: ")
# #     toDo_list[task] = description
# #     print(f"Задача '{task}' добавлена!\n")

# # print("\nВаш список задач:")
# # for task, desc in toDo_list.items():
# #     print(f"- {task}: {desc}")
