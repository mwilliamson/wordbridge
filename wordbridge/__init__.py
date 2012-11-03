import zipfile

from lxml import etree

import wordbridge.xmlparsing
import wordbridge.openxml
from wordbridge.htmlgeneration import HtmlGenerator
from wordbridge import styles

def convert_to_html(docx_file):
    document_string = docx_file.read("word/document.xml")
    tree = etree.fromstring(document_string)
    document = wordbridge.openxml.read_document(tree)
    
    generator = HtmlGenerator(paragraph_styles=_create_paragraph_styles())
    return generator.html_for_document(document).to_html_string()

def convert_docx_file_to_html(path):
    with zipfile.ZipFile(path, "r") as zip_file:
        return convert_to_html(zip_file)

def _create_paragraph_styles():
    return {
        "Heading1": styles.top_level_element("h1"),
        "Heading2": styles.top_level_element("h2"),
        "Heading3": styles.top_level_element("h3"),
        "Heading4": styles.top_level_element("h4"),
    }
