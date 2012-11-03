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

def _close_element(html_stack):
    html_stack.close_element()

def _sequence(*funcs):
    def apply(html_stack):
        for func in funcs:
            func(html_stack)
        
    return apply

def unordered_list():
    return Style(
        on_start=_sequence(
            _ensure_stack(ElementDescription("ul")),
            _open_element("li")
        ),
        on_end=_no_op
    )
    
class ElementDescription(object):
    def __init__(self, tag_name):
        self._tag_name = tag_name
        
    def matches(self, element):
        return element.tag_name == self._tag_name
        
    def create(self, factory):
        return factory(self._tag_name)
    
def _ensure_single_element_stack(tag_name):
    def apply(html_stack):
        current_element = html_stack.current_element()
        if current_element is None or current_element.tag_name != tag_name:
            html_stack.open_element(tag_name)
            
    return apply

def _no_op(self):
    return lambda html_stack: None

def _ensure_stack(*matchers):
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

class Style(object):
    def __init__(self, on_start, on_end):
        self._on_start = on_start
        self._on_end = on_end
        
    def start(self, html_stack):
        return self._on_start(html_stack)
        
    def end(self, html_stack):
        return self._on_end(html_stack)
