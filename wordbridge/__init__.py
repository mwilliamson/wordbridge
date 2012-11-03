import zipfile

from lxml import etree

import wordbridge.xmlparsing
import wordbridge.openxml
from wordbridge.htmlgeneration import HtmlGenerator
from wordbridge import styles

def convert_string_to_html(document_string):
    tree = etree.fromstring(document_string)
    document = wordbridge.openxml.read_document(tree)
    
    generator = HtmlGenerator(paragraph_styles=_create_paragraph_styles())
    return generator.html_for_document(document).to_html_string()

def convert_docx_file_to_html(path):
    with zipfile.ZipFile(path, "r") as zip_file:
        string = zip_file.read("word/document.xml")
        return convert_string_to_html(string)

def _create_paragraph_styles():
    return {
        "Heading1": styles.top_level_element("h1"),
        "Heading2": styles.top_level_element("h2"),
        "Heading3": styles.top_level_element("h3"),
        "Heading4": styles.top_level_element("h4"),
    }
