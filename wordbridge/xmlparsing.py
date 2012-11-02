from lxml import etree

def parse_string(string):
    return XmlElement(etree.fromstring(string))
    
class XmlElement(object):
    def __init__(self, element):
        self._element = element
        
    def xpath(self, xpath):
        elements = self._element.xpath(xpath, namespaces=_WORD_NAMESPACES)
        return map(self._wrap_element, elements)
    
    def text(self):
        return self._element.text
    
    def __repr__(self):
        return "XmlElement({0})".format(self._element.tag)
        
    def _wrap_element(self, element):
        if isinstance(element, basestring):
            return element
        else:
            return XmlElement(element)

_WORD_NAMESPACES = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
}
