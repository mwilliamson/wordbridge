from nose.tools import istest, assert_equal

from wordbridge.openxml.documents import read_document
from wordbridge import openxml
from wordbridge import xmlparsing

@istest
def word_document_containing_one_paragraph_is_read():
    document_xml = _create_document_xml("<w:p><w:r><w:t>Hello.</w:t></w:r></w:p>")
    
    result = read_document(document_xml)
    
    expected_document = openxml.document([
        openxml.paragraph([
            openxml.run([
                openxml.text("Hello.")
            ])
        ])
    ])
    assert_equal(expected_document, result)

@istest
def multiple_p_elements_are_read_as_multiple_paragraphs():
    document_xml = _create_document_xml(
        "<w:p><w:r><w:t>Hello</w:t></w:r></w:p>" +
        "<w:p><w:r><w:t>there</w:t></w:r></w:p>"
    )
    
    result = read_document(document_xml)
    
    expected_document = openxml.document([
        openxml.paragraph([
            openxml.run([
                openxml.text("Hello")
            ])
        ]),
        openxml.paragraph([
            openxml.run([
                openxml.text("there")
            ])
        ])
    ])
    assert_equal(expected_document, result)

@istest
def paragraph_style_is_read_from_paragraph_properties_element():
    document_xml = _create_document_xml(
        "<w:p>" + 
            """<w:pPr><w:pStyle w:val="Heading1"/></w:pPr>""" +
            "<w:r><w:t>Hello.</w:t></w:r>" +
        "</w:p>"
    )
    
    result = read_document(document_xml)
    
    expected_document = openxml.document([
        openxml.paragraph([
            openxml.run([
                openxml.text("Hello.")
            ])
        ], style="Heading1")
    ])
    assert_equal(expected_document, result)
    
@istest
def paragraph_style_is_read_from_paragraph_properties_element():
    document_xml = _create_document_xml("""
        <w:p> 
          <w:pPr>
            <w:pStyle w:val="ListParagraph"/>
            <w:numPr>
              <w:ilvl w:val="0"/>
              <w:numId w:val="1"/>
            </w:numPr>
          </w:pPr>
          <w:r><w:t>Hello.</w:t></w:r>
        </w:p>"""
    )
    
    result = read_document(document_xml)
    
    expected_document = openxml.document([
        openxml.paragraph([
            openxml.run([
                openxml.text("Hello.")
            ])
        ], style="ListParagraph", numbering_level=0)
    ])
    assert_equal(expected_document, result)

def _create_document_xml(inner_xml):
    return xmlparsing.parse_string(_WORD_DOCUMENT_TEMPLATE.format(inner_xml))

_WORD_DOCUMENT_TEMPLATE = """<?xml version="1.0" ?>
<w:document mc:Ignorable="w14 wp14" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
  <w:body>
    {0}
  </w:body>
</w:document>
"""
