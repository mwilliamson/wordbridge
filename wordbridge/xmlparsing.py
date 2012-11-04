from xml.dom import minidom
import xpath

def parse_string(string):
    return XmlNode(minidom.parseString(string))

class XmlNode(object):
    def __init__(self, node):
        self._node = node
        
    def find_nodes(self, expr):
        nodes = _xpath_context.find(expr, self._node)
        return map(XmlNode, nodes)
    
    def find_node(self, expr):
        return _single_or_none(self.find_nodes(expr))
    
    def find_values(self, expr):
        return [node.value for node in self.find_nodes(expr)]
    
    def find_value(self, expr):
        return _single_or_none(self.find_values(expr))
    
    def text(self):
        return self._node.data
    
    @property
    def value(self):
        return self._node.nodeValue
    
    def __repr__(self):
        return "XmlElement({0})".format(self._element.tag)
        
def _single_or_none(elements):
    length = len(elements)
    if length == 0:
        return None
    elif length == 1:
        return elements[0]
    else:
        raise RuntimeError("list has {0} elements".format(length))


_xpath_context = xpath.XPathContext()
_xpath_context.namespaces['w'] = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

_WORD_NAMESPACES = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
}
