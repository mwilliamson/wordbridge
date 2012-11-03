from wordbridge.html import HtmlBuilder

html = HtmlBuilder()

class HtmlStack(object):
    def __init__(self):
        self._fragment = html.fragment([])
        self._stack = []
        
    def open_element(self, tag_name):
        element = html.element(tag_name, [])
        self._add_child(element)
        self._stack.append(element)
    
    def close_element(self):
        popped = self._stack.pop()
    
    def text(self, text):
        self._add_child(html.text(text))
    
    def to_html_fragment(self):
        return self._fragment
    
    def current_element(self):
        if len(self._stack) == 0:
            return None
        else:
            return self._stack[-1]
    
    def __iter__(self):
        return iter(self._stack)
    
    def _add_child(self, child):
        self._peek().children.append(child)
        
    def _peek(self):
        if len(self._stack) == 0:
            return self._fragment
        else:
            return self._stack[-1]
