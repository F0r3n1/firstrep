import json

with open(r"C:\Users\f0r3n\Desktop\ваэно\pyproject\firstrep\dif_lvl\normal\toDo\toDo.json", "r") as file:
    toDo_listR = json.load(file)

def save():
    with open("toDo.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


while True:
    choice=input("Select an action: add / show / delete / exit: ").lower()
    
    def show():
        if len(toDo_listR) > 0:
            for index, (task, description) in enumerate(toDo_listR.items(), start=1):
                print(f"{index}. {task}: {description}")
        else:
            print("Пустой список")
    
    
    
    if choice=="add":
        toDo_listW=dict
        new_key = input("Введите название задачи (например, 'Покушать'): ")
        new_value = input("Опиши подробнее (например, 'Съесть пиццу'): ")

        toDo_listW[new_key] = new_value
        with open("C:\\Users\\f0r3n\\Desktop\\ваэно\\pyproject\\firstrep\\dif_lvl\\normal\\toDo\\toDo.json","w",ensure_ascii=False) as file:
            json.dump(toDo_listW,file)

    
    elif choice=="show":
        show()
    
    elif choice == "delete":
        show()
        toDelete = int(input("Выберете НОМЕР объекта, который хотите удалить: ")) - 1
        if input(f"Вы уверены что хотите удалить объект {toDo_list[toDelete]}? (yes/no): ").lower() == "yes":
            del toDo_list[toDelete]
            
        
        
    
    else:
        print("program terminated")
        break
    




with open("C:\\Users\\f0r3n\\Desktop\\ваэно\\pyproject\\firstrep\\dif_lvl\\normal\\toDo\\toDo.json","w") as file:
    json.dump(toDo_list,file)
    print(toDo_list)
