import time

status=True

while status==True:
    action=input("Введите команду (start / stop / exit): ").lower()
    if action=="start":
        start_sw=int(time.time())
        afterStartAction=input("Введите команду \"stop\" для остановки секундомера: ").lower()
        if afterStartAction=="stop":
            end_sw=int(time.time())
            print(f"Прошло около {end_sw-start_sw} секунд")
        elif afterStartAction=="exit":
            break
    elif action=="stop":
        print("Вы не запустили таймер")
    else:
        print("Выход из программы...")
        time.sleep(3)
        break




