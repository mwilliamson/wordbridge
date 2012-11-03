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
        return html_stack.to_html_fragment()

    def _generate_document_html(self, document, html_stack):
        for paragraph in document.paragraphs:
            self._generate_paragraph_html(paragraph, html_stack)
        
    def _generate_paragraph_html(self, paragraph, html_stack):
        style = self._find_paragraph_style(paragraph.style)
            
        style.start(html_stack)
            
        for run in paragraph.runs:
            for text in run.texts:
                html_stack.text(text.text)
                
        style.end(html_stack)
    
    def _find_paragraph_style(self, style_name):
        if style_name in self._paragraph_styles:
            return self._paragraph_styles[style_name]
        else:
            return _default_paragraph_mapping

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

_default_paragraph_mapping = mappings.top_level_element("p")
    
