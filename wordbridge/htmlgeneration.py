from wordbridge.html import HtmlBuilder

html = HtmlBuilder()

class HtmlGenerator(object):
    def __init__(self, paragraph_styles={}):
        self._paragraph_styles = paragraph_styles
    
    def html_for_document(self, document):
        return html.fragment(map(self.html_for_paragraph, document.paragraphs))

    def html_for_paragraph(self, paragraph):
        paragraph_text = []
        
        for run in paragraph.runs:
            for text in run.texts:
                paragraph_text.append(text.text)
        
        style = paragraph.style
        if style in self._paragraph_styles:
            style_mapping = self._paragraph_styles[style]
        else:
            style_mapping = default_paragraph_mapping
            
        return style_mapping([html.text("".join(paragraph_text))])
        

def default_paragraph_mapping(children):
    return html.element("p", children)
    
