from wordbridge.html import HtmlBuilder

html = HtmlBuilder()

def top_level_element(tag_name):
    return Style(
        on_start=_sequence(_clear_stack, _open_element(tag_name)),
        on_end=_clear_stack
    )

def _clear_stack(html_stack):
    while html_stack.current_element() is not None:
        html_stack.close_element()
        
def _open_element(tag_name):
    def apply(html_stack):
        html_stack.open_element(tag_name)
    
    return apply
    
def _sequence(*funcs):
    def apply(html_stack):
        for func in funcs:
            func(html_stack)
        
    return apply

def unordered_list():
    return UnorderedList()

class UnorderedList(object):
    def start(self, html_stack):
        current_element = html_stack.current_element()
        if current_element is None or current_element.tag_name != "ul":
            html_stack.open_element("ul")
        html_stack.open_element("li")
        
    def end(self, html_stack):
        html_stack.close_element()

class Style(object):
    def __init__(self, on_start, on_end):
        self._on_start = on_start
        self._on_end = on_end
        
    def start(self, html_stack):
        return self._on_start(html_stack)
        
    def end(self, html_stack):
        return self._on_end(html_stack)
