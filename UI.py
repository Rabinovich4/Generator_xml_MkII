from tkinter import *
from tkinter import ttk
from lxml import etree
from tkinter import filedialog
from new_values import get_random_int
from parsing_xml import namespaces, parsing_contragent_xml_file, parsing_user_xml_file

# Начало окна ткинтера
root = Tk()
root.title('Generator_xml MkII')
root.geometry('500x500')

# Инициализация Notebook
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Вкладка с контрагентом
kontragent_tab = ttk.Frame(notebook)
notebook.add(kontragent_tab, text='Контрагент')

label = Label(kontragent_tab, text='Введите ИНН')
label.pack()
entry_inn = ttk.Entry(kontragent_tab)
entry_inn.pack()

label = Label(kontragent_tab, text='Введите КПП')
label.pack()
entry_kpp = ttk.Entry(kontragent_tab)
entry_kpp.pack()

label = Label(kontragent_tab, text='Введите ОГРН')
label.pack()
entry_ogrn = ttk.Entry(kontragent_tab)
entry_ogrn.pack()

label = Label(kontragent_tab, text='Введите Полное наименование организации')
label.pack()
entry_full_name = ttk.Entry(kontragent_tab)
entry_full_name.pack()

class ContragentParams:
    def __init__(self):
        self.root = parsing_contragent_xml_file()

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

    def get_full_name(self):
        input_full_name = entry_full_name.get()
        if input_full_name == '':
            root = self.root
            input_full_name = root.xpath('.//eruz:legalEntityRFDataInfo/eruz:fullName/text()', namespaces=namespaces)[0]
        else:
            input_full_name = input_full_name
        return input_full_name

    def refactor_contragent_data(self):
        root = self.root
        tree = etree.ElementTree(root)
        output_file = 'contragent.xml'

        # Получение значения полного наименования организации и разделение на Еруз/номер
        full_name = self.get_full_name()
        name_part = full_name.split()[0]  # Предполагается, что "Еруз" - это первое слово
        number_part = ''.join(filter(str.isdigit, full_name))
        new_number = int(number_part) + 1 if number_part else 1
        new_full_name = f"{name_part} {new_number}"

        # Замена значений INN, KPP, OGRN на случайные
        root.xpath('.//eruz:legalEntityRFDataInfo/eruz:INN', namespaces=namespaces)[0].text = str(self.get_inn())
        root.xpath('.//eruz:legalEntityRFDataInfo/eruz:KPP', namespaces=namespaces)[0].text = str(self.get_kpp())
        root.xpath('.//eruz:legalEntityRFDataInfo/eruz:OGRN', namespaces=namespaces)[0].text = str(self.get_ogrn())

        # Замена значений objectId, registryNum, fullName на случайные + имя на Еруз номер +1
        object_id = str(get_random_int(9))
        registry_num = str(get_random_int(9))
        root.xpath('.//default:objectId', namespaces=namespaces)[0].text = object_id
        root.xpath('.//eruz:registryNum', namespaces=namespaces)[0].text = registry_num

        root.xpath('.//eruz:fullName', namespaces=namespaces)[0].text = new_full_name
        root.xpath('.//cmn:email', namespaces=namespaces)[0].text = f"eruz-elkkkkk{new_number}@mailforspam.com"
        root.xpath('.//cmn:notificationEmail', namespaces=namespaces)[0].text = f"eruz-elkkkkk{new_number}@mailforspam.com"

        # Сохранение файла контрагента в директорию по выбору пользователя
        save_path = filedialog.asksaveasfilename(defaultextension=".xml",
                                                 filetypes=[("XML files", "*.xml"), ("All files", "*.*")])
        if save_path:
            tree.write(save_path, pretty_print=True, xml_declaration=True, encoding='UTF-8')

        # Сохранение в файл output_file внутри проекта
        tree.write(output_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Создаем экземпляр класса ContragentParams
contragent_params_data = ContragentParams()

# Привязываем метод refactor_contragent_data к кнопке
btn_generate_contragent = ttk.Button(kontragent_tab, text='Сгенерировать',
                                     command=contragent_params_data.refactor_contragent_data)
btn_generate_contragent.pack()

# Вкладка с юзером
user_tab = ttk.Frame(notebook)
notebook.add(user_tab, text='Юзер')

label = Label(user_tab, text='Введите Фамилию')
label.pack()
entry_last_name = ttk.Entry(user_tab)
entry_last_name.pack()

label = Label(user_tab, text='Введите Имя')
label.pack()
entry_first_name = ttk.Entry(user_tab)
entry_first_name.pack()

label = Label(user_tab, text='Введите Отчество')
label.pack()
entry_middle_name = ttk.Entry(user_tab)
entry_middle_name.pack()

class UserParams:
    def __init__(self):
        self.root = parsing_user_xml_file()

    def get_last_name(self):
        input_last_name = entry_last_name.get()
        if input_last_name == '':
            raise ValueError('Поле не может быть пустым')
        return input_last_name

    def get_first_name(self):
        input_first_name = entry_first_name.get()
        if input_first_name == '':
            raise ValueError('Поле не может быть пустым')
        return input_first_name

    def get_middle_name(self):
        input_middle_name = entry_middle_name.get()
        if input_middle_name == '':
            raise ValueError('Поле не может быть пустым')
        return input_middle_name

    def refactor_user_data(self):
        root = self.root
        tree = etree.ElementTree(root)
        output_user_file = 'user.xml'

        root.xpath('.//ns2:lastName', namespaces=namespaces)[0].text = str(self.get_last_name())
        root.xpath('.//ns2:firstName', namespaces=namespaces)[0].text = str(self.get_first_name())
        root.xpath('.//ns2:middleName', namespaces=namespaces)[0].text = str(self.get_middle_name())

        # Сохранение файла юзера в директорию по выбору пользователя
        save_path = filedialog.asksaveasfilename(defaultextension=".xml",
                                                 filetypes=[("XML files", "*.xml"), ("All files", "*.*")])
        if save_path:
            tree.write(save_path, pretty_print=True, xml_declaration=True, encoding='UTF-8')

        # Сохранение в файл output_file внутри проекта
        tree.write(output_user_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Создаем экземпляр класса UserParams
user_params_data = UserParams()

# Привязываем метод chek к кнопке
btn_generate_user = ttk.Button(user_tab, text='Сгенерировать',
                               command=user_params_data.refactor_user_data)
btn_generate_user.pack()

# Конец окна ткинтера
root.mainloop()