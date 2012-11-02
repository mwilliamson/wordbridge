import collections

import wordbridge.xmlparsing

def read_document(tree):
    tree = wordbridge.xmlparsing.XmlElement(tree)
    return Document(map(_read_paragraph, tree.xpath("//w:p")))
    
def _read_paragraph(element):
    return Paragraph(map(_read_run, element.xpath("w:r")))
    
def _read_run(element):
    return Run(map(_read_text, element.xpath("w:t")))
    
def _read_text(element):
    return Text(element.text())
    
Document = collections.namedtuple("Document", ["paragraphs"])

Paragraph = collections.namedtuple("Paragraph", ["runs"])

Run = collections.namedtuple("Run", ["texts"])

Text = collections.namedtuple("Text", ["text"])
