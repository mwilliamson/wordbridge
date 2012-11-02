class HtmlGenerator(object):
    def for_document(self, document):
        return "".join(map(self.for_paragraph, document.paragraphs))

    def for_paragraph(self, paragraph):
        paragraph_text = []
        
        for run in paragraph.runs:
            for text in run.texts:
                paragraph_text.append(text.text)
        
        return "<p>{0}</p>".format("".join(paragraph_text))

    
