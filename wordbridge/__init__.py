from lxml import etree

import wordbridge.xmlparsing
from wordbridge.htmlgeneration import HtmlGenerator

def convert_string_to_html(document_string):
    tree = etree.fromstring(document_string)
    document = wordbridge.openxml.read_document(tree)
    
    generator = HtmlGenerator()
    return generator.for_document(document)

