from wordbridge.html import HtmlBuilder

html = HtmlBuilder()

class HtmlGenerator(object):
    def html_for_document(self, document):
        return html.fragment(map(self.html_for_paragraph, document.paragraphs))

    def html_for_paragraph(self, paragraph):
        paragraph_text = []
        
        for run in paragraph.runs:
            for text in run.texts:
                paragraph_text.append(text.text)
        
        return html.element("p", [html.text("".join(paragraph_text))])

    
