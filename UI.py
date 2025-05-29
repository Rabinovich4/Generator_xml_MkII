from tkinter import *
from tkinter import ttk
from lxml import etree
from tkinter import filedialog
import string
from new_values import get_random_int
from parsing_xml import namespaces, parsing_xml_file

root = Tk()     # начало окна ткинтера
root.title('Generator_xml MkII')
root.geometry('500x500')

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

class Knopki:
    def __init__(self):
        self.root = parsing_xml_file()

    def get_inn(self):
        input_inn = entry_inn.get()
        if input_inn == '':
            input_inn = get_random_int(9)
        else:
            input_inn = int(input_inn)
        return input_inn

    def get_kpp(self):
        input_kpp = entry_kpp.get()
        if input_kpp == '':
            input_kpp = get_random_int(9)
        else:
            input_kpp = int(input_kpp)
        return input_kpp

    def get_ogrn(self):
        input_ogrn = entry_ogrn.get()
        if input_ogrn == '':
            input_ogrn = get_random_int(13)
        else:
            input_ogrn = int(input_ogrn)
        return input_ogrn

    def chek(self):
        root = self.root
        tree = etree.ElementTree(root)
        output_file = 'contragent.xml'

        fullName = root.xpath('.//eruz:legalEntityRFDataInfo/eruz:fullName/text()', namespaces=namespaces)[0]
        email = root.xpath('.//cmn:email/text()', namespaces=namespaces)[0]
        notificationEmail = root.xpath('.//cmn:notificationEmail/text()', namespaces=namespaces)[0]

        # Замена значения INN, KPP, OGRN на случайные
        root.xpath('.//eruz:legalEntityRFDataInfo/eruz:INN', namespaces=namespaces)[0].text = str(self.get_inn())
        root.xpath('.//eruz:legalEntityRFDataInfo/eruz:KPP', namespaces=namespaces)[0].text = str(self.get_kpp())
        root.xpath('.//eruz:legalEntityRFDataInfo/eruz:OGRN', namespaces=namespaces)[0].text = str(self.get_ogrn())

        # Замена значения objectId, registryNum, fullName на случайные + имя на Еруз номер +1
        root.xpath('.//default:objectId', namespaces=namespaces)[0].text = str(get_random_int(9))
        root.xpath('.//eruz:registryNum', namespaces=namespaces)[0].text = str(get_random_int(9))

        name_part = fullName[:5]  # "Еруз "
        number_part = fullName[5:]  # " номер"
        new_number = int(number_part) + 1

        root.xpath('.//eruz:fullName', namespaces=namespaces)[0].text = f"{name_part}{new_number}"
        root.xpath('.//cmn:email', namespaces=namespaces)[0].text = f"eruz-elkkkkk{new_number}@mailforspam.com"
        root.xpath('.//cmn:notificationEmail', namespaces=namespaces)[0].text = f"eruz-elkkkkk{new_number}@mailforspam.com"

        save_path = filedialog.asksaveasfilename(defaultextension=".xml",
                                                 filetypes=[("XML files", "*.xml"), ("All files", "*.*")])
        tree.write(output_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')
        if not save_path:
            return

        # Форматируем XML с отступами
        xml_str = etree.tostring(root, pretty_print=True, encoding='utf-8', xml_declaration=True)
        with open(save_path, 'wb') as f:
            f.write(xml_str)

# Создаем экземпляр класса Knopki
knopki_instance = Knopki()

# Привязываем метод chek к кнопке
btn_generate = ttk.Button(text='Сгенерировать', command=knopki_instance.chek)
btn_generate.pack()

root.mainloop()  # конец окна ткинтера