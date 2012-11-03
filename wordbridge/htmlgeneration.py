from wordbridge.html import HtmlBuilder
from wordbridge import mappings

html = HtmlBuilder()

class HtmlGenerator(object):
    def __init__(self, paragraph_styles={}):
        self._paragraph_styles = paragraph_styles
    
    def html_for_document(self, document):
        return self._html_for(self._generate_document_html, document)

    def html_for_paragraph(self, paragraph):
        return self._html_for(self._generate_paragraph_html, paragraph)

    def _html_for(self, generator, element):
        html_stack = HtmlStack()
        generator(element, html_stack)
        html_stack.finish()
        return html_stack.to_html_fragment()

    def _generate_document_html(self, document, html_stack):
        for paragraph in document.paragraphs:
            self._generate_paragraph_html(paragraph, html_stack)
        
    def _generate_paragraph_html(self, paragraph, html_stack):
        style = paragraph.style
        if style in self._paragraph_styles:
            style_mapping = self._paragraph_styles[style]
        else:
            style_mapping = _default_paragraph_mapping
            
        style_mapping.start(html_stack)
            
        for run in paragraph.runs:
            for text in run.texts:
                html_stack.text(text.text)
                
        style_mapping.end(html_stack)
        

class HtmlStack(object):
    def __init__(self):
        self._fragment = html.fragment([])
        self._stack = []
        
    def open(self, tag_name):
        self._stack.append(html.element(tag_name, []))
    
    def close(self):
        popped = self._stack.pop()
        self._add_child(popped)
    
    def text(self, text):
        self._add_child(html.text(text))
    
    def finish(self):
        while len(self._stack) != 0:
            self.close()
    
    def to_html_fragment(self):
        return self._fragment
    
    def current_element(self):
        if len(self._stack) == 0:
            return None
        else:
            return self._stack[-1]
    
    def _add_child(self, child):
        self._peek().children.append(child)
        
    def _peek(self):
        if len(self._stack) == 0:
            return self._fragment
        else:
            return self._stack[-1]

_default_paragraph_mapping = mappings.top_level_element("p")
    
