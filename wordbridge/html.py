import collections
import cgi

class HtmlBuilder(object):
    def element(self, tag_name, children):
        return HtmlElement(tag_name, children) 
    
    def fragment(self, children):
        return HtmlFragment(children)
    
    def text(self, text):
        return HtmlTextNode(text)

HtmlElementBase = collections.namedtuple("HtmlElement", ["tag_name", "children"])

class HtmlElement(HtmlElementBase):
    def to_html_string(self):
        children_html = "".join(child.to_html_string() for child in self.children)
        return "<{0}>{1}</{0}>".format(self.tag_name, children_html)

HtmlTextNodeBase = collections.namedtuple("HtmlTextNode", ["text"])

class HtmlTextNode(HtmlTextNodeBase):
    def to_html_string(self):
        return _html_escape(self.text)

HtmlFragmentBase = collections.namedtuple("HtmlFragment", ["children"])

class HtmlFragment(HtmlFragmentBase):
    def to_html_string(self):
        return "".join(child.to_html_string() for child in self.children)

def _html_escape(string):
    return cgi.escape(string, quote=True)
