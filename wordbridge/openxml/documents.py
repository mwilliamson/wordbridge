import collections

import wordbridge.xmlparsing

def read_document(tree):
    tree = wordbridge.xmlparsing.XmlElement(tree)
    return document(map(_read_paragraph, tree.xpath("//w:p")))
    
def _read_paragraph(element):
    style = element.single_xpath("w:pPr/w:pStyle/@w:val")
    return paragraph(map(_read_run, element.xpath("w:r")), style=style)
    
def _read_run(element):
    return run(map(_read_text, element.xpath("w:t")))
    
def _read_text(element):
    return text(element.text())

Document = collections.namedtuple("Document", ["paragraphs"])
Paragraph = collections.namedtuple("Paragraph", ["runs", "style"])
Run = collections.namedtuple("Run", ["texts"])
Text = collections.namedtuple("Text", ["text"])

document = Document

def paragraph(runs, style=None):
    return Paragraph(runs, style)

run = Run

text = Text
