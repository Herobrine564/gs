from tkinter import *
from tkinter import ttk

clicks = 0

def show_message():
    label["text"] = entry.get()

def click_button():
    global clicks
    clicks += 1
    btn["text"] = f"Задача добавлена {clicks}"


def reset_clicks():
    global clicks
    clicks == 0
    btn1["text"] = f"Сбросить"

root = Tk()
root.title("Заголовок приложения")
root.geometry("460x520")

entry = ttk.Entry()
entry.pack(anchor=NW, padx=8, pady= 8)

btn = ttk.Button(text="Добавить задачу", command=show_message and click_button)
btn1 = ttk.Button(text="Сбросить", command=reset_clicks)
btn.pack()

python_logo = PhotoImage(file="img1.png")

label = ttk.Label(image=python_logo, text="Здесь отобразятся сколько было добавлено задач", compound="top")
label.pack()

root.mainloop()