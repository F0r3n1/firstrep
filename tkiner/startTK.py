import tkinter as tk
from tkinter import font

root= tk.Tk()

root.iconbitmap("firstrep\\sources\\img\\icon.ico")
root.title("Окно")
root.geometry("600x900")
root.resizable(width=False, height=False)


# label = tk.Label(root, text="text", font=("", 10))
# label.pack(pady=200)

def click():
    print("вывод попа")
btn=tk.Button(root, text="Кнопка", command=click, font=("Segoe UI Variable Small Semibol", 20,'bold'), background='white', activebackground="grey" )
btn.pack()

label=tk.Label(root, text="Кнопка", font=("Segoe UI Variable Small Semibol", 20,'bold'), background='white', activebackground="grey" )
label.pack()


print(font.families())
root.config(background="pink")


root.mainloop()