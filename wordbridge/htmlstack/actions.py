from wordbridge.html import HtmlBuilder

html = HtmlBuilder()

def no_op(self):
    return lambda html_stack: None
    
def clear_stack(html_stack):
    while html_stack.current_element() is not None:
        html_stack.close_element()
        
def open_element(tag_name):
    def apply(html_stack):
        html_stack.open_element(tag_name)
    
    return apply

def close_element(html_stack):
    html_stack.close_element()

def sequence(*funcs):
    def apply(html_stack):
        for func in funcs:
            func(html_stack)
        
    return apply
    
def ensure_stack(*matchers):
    def partial_match(html_stack):
        for existing_element, matcher in map(None, html_stack, matchers):
            if existing_element is None:
                return True
            if matcher is None or not matcher.matches(existing_element):
                return False
        return True
    
    def apply(html_stack):
        while not partial_match(html_stack):
            html_stack.close_element()
        for existing_element, matcher in map(None, html_stack, matchers):
            if existing_element is None:
                matcher.create(html_stack.open_element)
        
    return apply
    
class ElementDescription(object):
    def __init__(self, tag_name):
        self._tag_name = tag_name
        
    def matches(self, element):
        return element.tag_name == self._tag_name
        
    def create(self, factory):
        return factory(self._tag_name)
