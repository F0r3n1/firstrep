spamwords=["казино", "заработай", "бесплатно", "вложи", "крипта", "биткоин", "кредит", "выиграй", "прибыль", "доход"]
text=input("Введите сообщение:")
antispam=text.lower().split()
def antispamfunc():
    for i in antispam:
        if i in text:
            print("ТЕКСТ СО СПАМОМ")
            break

antispamfunc()