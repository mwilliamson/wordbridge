import zipfile

import wordbridge.xmlparsing
import wordbridge.openxml
from wordbridge import openxml
from wordbridge.htmlgeneration import HtmlGenerator
from wordbridge import styles

def convert_to_html(docx_file):
    document_string = docx_file.read("word/document.xml")
    tree = wordbridge.xmlparsing.parse_string(document_string)
    document = wordbridge.openxml.read_document(tree)
    
    generator = HtmlGenerator(paragraph_styles=_create_paragraph_styles())
    return generator.html_for_document(document).to_html_string()

def convert_docx_file_to_html(path):
    with zipfile.ZipFile(path, "r") as zip_file:
        return convert_to_html(zip_file)

def _create_paragraph_styles():
    return [
        styles.map_word_style("Heading1").to(styles.top_level_element("h1")),
        styles.map_word_style("Heading2").to(styles.top_level_element("h2")),
        styles.map_word_style("Heading3").to(styles.top_level_element("h3")),
        styles.map_word_style("Heading4").to(styles.top_level_element("h4")),
        styles.map_word_style("ListParagraph", numbering_level=0).to(styles.unordered_list(depth=1)),
        styles.map_word_style("ListParagraph", numbering_level=1).to(styles.unordered_list(depth=2)),
        styles.map_word_style("ListParagraph", numbering_level=2).to(styles.unordered_list(depth=3)),
        styles.map_word_style("ListParagraph", numbering_level=3).to(styles.unordered_list(depth=4))
    ]
