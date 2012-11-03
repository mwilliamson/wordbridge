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

def map_word_style(*args, **kwargs):
    return MappingBuilder(*args, **kwargs)
    
class MappingBuilder(object):
    def __init__(self, style_name, numbering_level=None):
        self._style_name = style_name
        self._numbering_level = numbering_level
    
    def matches(self, paragraph):
        if paragraph.style != self._style_name:
            return False
        if paragraph.numbering_level != self._numbering_level:
            return False
        return True
    
    def to(self, style):
        return Mapping(self.matches, style)
        
class Mapping(object):
    def __init__(self, word_style_matcher, style):
        self._word_style_matcher = word_style_matcher
        self.style = style

    def matches(self, paragraph):
        return self._word_style_matcher(paragraph)
    
