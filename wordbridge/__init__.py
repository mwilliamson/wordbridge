from lxml import etree

import wordbridge.xmlparsing

def convert_string_to_html(document_string):
    tree = etree.fromstring(document_string)
    document = wordbridge.openxml.read_document(tree)
    return _convert_document_to_html(document)

def _convert_document_to_html(document):
    return "".join(map(_convert_paragraph_to_html, document.paragraphs))

def _convert_paragraph_to_html(paragraph):
    paragraph_text = []
    
    for run in paragraph.runs:
        for text in run.texts:
            paragraph_text.append(text.text)
    
    return "<p>{0}</p>".format("".join(paragraph_text))
