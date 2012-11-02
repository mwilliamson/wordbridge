from lxml import etree

def parse_string(string):
    return XmlElement(etree.fromstring(string))
    
class XmlElement(object):
    def __init__(self, element):
        self._element = element
        
    def xpath(self, xpath):
        return map(XmlElement, self._element.xpath(xpath, namespaces=_WORD_NAMESPACES))
    
    def text(self):
        return self._element.text
    
    def __repr__(self):
        return "XmlElement({0})".format(self._element.tag)

_WORD_NAMESPACES = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
}
