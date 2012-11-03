from wordbridge import styles
from wordbridge.htmlstack import HtmlStack

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

_default_paragraph_mapping = styles.top_level_element("p")
    
