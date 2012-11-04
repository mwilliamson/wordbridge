import collections

def read_document(tree):
    return document(map(_read_paragraph, tree.find_nodes("//w:p")))
    
def _read_paragraph(element):
    style = element.find_value("w:pPr/w:pStyle/@w:val")
    numbering_level = element.find_value("w:pPr/w:numPr/w:ilvl/@w:val")
    if numbering_level is not None:
        numbering_level = int(numbering_level)
    return paragraph(
        map(_read_run, element.find_nodes("w:r")),
        style=style,
        numbering_level=numbering_level
    )
    
def _read_run(element):
    return run(map(_read_text, element.find_nodes("w:t")))
    
def _read_text(text_node):
    return text(text_node.find_value("text()"))

Document = collections.namedtuple("Document", ["paragraphs"])
Paragraph = collections.namedtuple("Paragraph", ["runs", "style", "numbering_level"])
Run = collections.namedtuple("Run", ["texts"])
Text = collections.namedtuple("Text", ["text"])

document = Document

def paragraph(runs, style=None, numbering_level=None):
    return Paragraph(runs, style, numbering_level)

run = Run

text = Text
