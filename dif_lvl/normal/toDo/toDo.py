import json

with open(r"C:\Users\f0r3n\Desktop\ваэно\pyproject\firstrep\dif_lvl\normal\toDo\toDo.json", "r",encoding="utf-8") as file:
    toDo_listR = json.load(file)


def save():
        with open("C:\\Users\\f0r3n\\Desktop\\ваэно\\pyproject\\firstrep\\dif_lvl\\normal\\toDo\\toDo.json", "w", encoding="utf-8") as file:
            json.dump(toDo_listR or toDo_list, file, ensure_ascii=False, indent=4)

while True:
    choice=input("Select an action: add / show / delete / exit: ").lower()
    
    def show():
        if len(toDo_listR) > 0:
            for index, (task, description) in enumerate(toDo_listR.items(), start=1):
                print(f"{index}. {task}: {description}")
        else:
            print("Пустой список")
    
    
    
    with open("C:\\Users\\f0r3n\\Desktop\\ваэно\\pyproject\\firstrep\\dif_lvl\\normal\\toDo\\toDo.json", "r", encoding="utf-8") as file:
        toDo_list = json.load(file)

    if choice == "add":
        new_key = input("Введите название задачи (например, 'Покушать'): ")
        new_value = input("Опиши подробнее (например, 'Съесть пиццу'): ")

        toDo_list[new_key] = new_value
        save()

    
    elif choice=="show":
        show()
    
    elif choice == "delete":
        show()
        key_to_delete = input("Введите точное название задачи, которую хотите удалить: ")


        if key_to_delete in toDo_listR:
            del toDo_listR[key_to_delete]
            save()     
            print(f"Задача '{key_to_delete}' удалена.")
        else:
            print("Такой задачи нет.")
        
    
    else:
        print("program terminated")
        break
    



