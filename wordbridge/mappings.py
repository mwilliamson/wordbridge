from wordbridge.html import HtmlBuilder

html = HtmlBuilder()

def top_level_element(tag_name):
    return TopLevelElement(tag_name)

class TopLevelElement(object):
    def __init__(self, tag_name):
        self._tag_name = tag_name
    
    def start(self, html_stack):
        html_stack.open_element(self._tag_name)
        
    def end(self, html_stack):
        html_stack.close_element()
        

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
