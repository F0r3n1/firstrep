import json


PATH=r"C:\Users\f0r3n\Desktop\ваэно\pyproject\firstrep\dif_lvl\normal\moviesFounder\movies.json"

def save(data):
    with open(PATH, "w", encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False, indent=4,)

def load():
    try:
        with open(PATH, "r", encoding="utf-8") as file:
            return json.load(file) 
    except FileNotFoundError:
        return []  
    except json.JSONDecodeError:
        return []  


def show():
    movies=load()
    if not movies:
        print("empty")
    else:
        for index,film in enumerate(movies):
            print(f"{index+1}. {film['film']} ({film['year']}) — рейтинг: {film['rating']}")
            print(f"   Описание: {film['description']}")

while True:
    userChoice=input("Выберите действие: add / show / delete / search / exit: ").lower()

    if userChoice=="add":
        movName=input("Введите название фильма: ")
        movYear=int(input("Введите год издания: "))
        movRate=float(input("Введите рейтинг филма: "))
        MovDescr=input("Введите описаеме фильма: ")
        film={
            "film":movName,
            "year":movYear,
            "rating":movRate,
            "description":MovDescr
        }
        movies = load()      
        movies.append(film)  
        save(movies)
    
    
    elif userChoice=="show":
        show()
    
    
    elif userChoice=="delete":
        print("Выберите, что хотите удалить")
        show()
        toDelete=int(input("Введите номер фильма, который хотите удалить: "))-1
        movies=load()
        movies.pop(toDelete)
        save(movies)
    
    
    elif userChoice == "search":
        searchWord = input("Введите название фильма (без ошибок, но можно не полностью): ").lower()
        founded = []
        movies = load()
        for video in movies:
            if searchWord in video["film"].lower():
                founded.append(video)
        if founded:
            for index, video in enumerate(founded, start=1):
                print(f"{index}. {video['film']} ({video['year']}) — рейтинг: {video['rating']}")
                print(f"   Описание: {video['description']}")
        else:
            print("Фильмы с таким названием не найдены.")
    
    
    else:
        print("Выход из программы...")
        break
    

