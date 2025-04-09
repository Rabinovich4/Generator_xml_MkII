from lxml import etree

# Пространства имён
namespaces = {
    'eruz': 'http://zakupki.gov.ru/eruz/types/1',
    'cmn': 'http://zakupki.gov.ru/eruz/common/1',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    'default': 'http://zakupki.gov.ru/eruz/integration/1'
}


# Чтение XML файла
def parsing_xml_file():
    file = 'contragent.xml'
    doc = etree.parse(file)
    root_doc = doc.getroot()
    return root_doc



# inn = root.xpath('.//eruz:legalEntityRFDataInfo/eruz:INN/text()', namespaces=namespaces)
# kpp = root.xpath('.//eruz:legalEntityRFDataInfo/eruz:KPP/text()', namespaces=namespaces)
# ogrn = root.xpath('.//eruz:legalEntityRFDataInfo/eruz:OGRN/text()', namespaces=namespaces)

