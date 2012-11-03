from wordbridge.html import HtmlBuilder
from wordbridge.htmlstack import actions

html = HtmlBuilder()

def top_level_element(tag_name):
    return Style(
        on_start=actions.sequence(
            actions.clear_stack,
            actions.open_element(tag_name)
        ),
        on_end=actions.clear_stack
    )

def unordered_list(depth=1):
    descriptions = []
    for i in range(0, depth - 1):
        descriptions.append(actions.ElementDescription("ul"))
        descriptions.append(actions.ElementDescription("li"))
    descriptions.append(actions.ElementDescription("ul"))
    
    return Style(
        on_start=actions.sequence(
            actions.ensure_stack(*descriptions),
            actions.open_element("li")
        ),
        on_end=actions.no_op
    )

class Style(object):
    def __init__(self, on_start, on_end):
        self._on_start = on_start
        self._on_end = on_end
        
    def start(self, html_stack):
        return self._on_start(html_stack)
        
    def end(self, html_stack):
        return self._on_end(html_stack)
