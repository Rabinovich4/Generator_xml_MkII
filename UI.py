import string
from tkinter import *
from tkinter import ttk

root = Tk()     # начало окнта ткинтера
root.title('Generator_xml MkII')
root.geometry('500x500')

# entry = ttk.Entry(root)
# entry.pack()

label = Label(text='Введите ИНН')
label.pack()
entry_inn = ttk.Entry()
entry_inn.pack()

label = Label(text='Введите КПП')
label.pack()
entry_kpp = ttk.Entry()
entry_kpp.pack()

label = Label(text='Введите ОГРН')
label.pack()
entry_ogrn = ttk.Entry()
entry_ogrn.pack()

digits = ''.join(string.digits)


def generate_xml():
    user_input = entry.get()
    if user_input == '':
        user_input = 10
    else:
        user_input = int(user_input)


btn_generate = ttk.Button(text='Сгенерировать', command=generate_xml)
btn_generate.pack()

root.mainloop()  # конец окна ткинтера