import random
import string

from parsing_xml import namespaces, parsing_xml_file


def get_random_int(number_of_digits: int = 9) -> str:
    """Метод возвращает рандомное число с длиной <number_of_digits> символов."""
    digits = string.digits
    new_random_int = "".join(random.choices(digits, k=number_of_digits))
    return new_random_int.lstrip("0").ljust(number_of_digits, random.choice(digits))


# inn = parsing_xml_file().xpath('.//eruz:legalEntityRFDataInfo/eruz:INN/text()', namespaces=namespaces)
# kpp = parsing_xml_file().xpath('.//eruz:legalEntityRFDataInfo/eruz:KPP/text()', namespaces=namespaces)
# ogrn = parsing_xml_file().xpath('.//eruz:legalEntityRFDataInfo/eruz:OGRN/text()', namespaces=namespaces)
