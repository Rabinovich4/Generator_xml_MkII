from lxml import etree

import random
import string

from parsing_xml import namespaces, parsing_xml_file

# output_file = 'new_contragent.xml'
output_file = 'contragent.xml'

root = parsing_xml_file()

tree = etree.ElementTree(root)


def get_random_int(number_of_digits: int = 9) -> str:
    """Метод возвращает рандомное число с длиной <number_of_digits> символов."""
    digits = string.digits
    new_random_int = "".join(random.choices(digits, k=number_of_digits))
    return new_random_int.lstrip("0").ljust(number_of_digits, random.choice(digits))


# Если нужно получить элемент из списка
# inn = parsing_xml_file().xpath('.//eruz:legalEntityRFDataInfo/eruz:INN/text()', namespaces=namespaces)[0]
# kpp = parsing_xml_file().xpath('.//eruz:legalEntityRFDataInfo/eruz:KPP/text()', namespaces=namespaces)[0]
# ogrn = parsing_xml_file().xpath('.//eruz:legalEntityRFDataInfo/eruz:OGRN/text()', namespaces=namespaces)[0]
fullName = root.xpath('.//eruz:legalEntityRFDataInfo/eruz:fullName/text()', namespaces=namespaces)[0]
email = root.xpath('.//cmn:email/text()', namespaces=namespaces)[0]
notificationEmail = root.xpath('.//cmn:notificationEmail/text()', namespaces=namespaces)[0]
# Замена значения INN, KPP, OGRN на случайные
# root.xpath('.//eruz:legalEntityRFDataInfo/eruz:INN', namespaces=namespaces)[0].text = get_random_int()
# root.xpath('.//eruz:legalEntityRFDataInfo/eruz:KPP', namespaces=namespaces)[0].text = get_random_int()
# root.xpath('.//eruz:legalEntityRFDataInfo/eruz:OGRN', namespaces=namespaces)[0].text = get_random_int()

# Замена значения objectId, registryNum, fullName на случайные + имя на Еруз номер +1
root.xpath('.//default:objectId', namespaces=namespaces)[0].text = get_random_int(9)
root.xpath('.//eruz:registryNum', namespaces=namespaces)[0].text = get_random_int(9)

name_part = fullName[:5]  # "Еруз "
number_part = fullName[5:]  # "номер"
new_number = int(number_part) + 1

root.xpath('.//eruz:fullName', namespaces=namespaces)[0].text = f"{name_part}{new_number}"
root.xpath('.//cmn:email', namespaces=namespaces)[0].text = f"eruz-elkkkkk{new_number}@mailforspam.com"
root.xpath('.//cmn:notificationEmail', namespaces=namespaces)[0].text = f"eruz-elkkkkk{new_number}@mailforspam.com"


tree.write(output_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')