from wordbridge.html import HtmlBuilder

html = HtmlBuilder()

def top_level_element(tag_name):
    def mapping(children):
        return html.element(tag_name, children)
    
    return mapping
