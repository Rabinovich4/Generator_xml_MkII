from lxml import etree

# Пространства имён
namespaces = {
    'eruz': 'http://zakupki.gov.ru/eruz/types/1',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    'as2': 'http://zakupki.gov.ru/eruz/integration/1',
    'base': 'http://zakupki.gov.ru/eruz/base/1',
    'cmn': 'http://zakupki.gov.ru/eruz/common/1',
    'ns3': 'http://zakupki.gov.ru/eruz/nsi/1',
    'ns2': 'http://zakupki.gov.ru/eruz/common/1',
    'int': 'http://zakupki.gov.ru/eruz/internal/1',
    'bus': 'http://zakupki.gov.ru/busMonitoring',
    'sm': 'http://zakupki.gov.ru/eruz/SMTypes/1',
    'default': 'http://zakupki.gov.ru/eruz/integration/1'
}


# Чтение XML файла
def parsing_contragent_xml_file():
    file = 'contragent.xml'
    doc = etree.parse(file)
    root_doc = doc.getroot()
    return root_doc


def parsing_user_xml_file():
    file = 'user.xml'
    doc = etree.parse(file)
    root_doc = doc.getroot()
    return root_doc


