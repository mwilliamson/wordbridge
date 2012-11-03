from nose.tools import istest, assert_equal

import wordbridge

@istest
def word_document_containing_one_pararaph_is_converted_to_single_p_element():
    docx_file = FakeDocxFile({
        "word/document.xml": _SIMPLE_WORD_DOCUMENT
    })
    result = wordbridge.convert_to_html(docx_file)
    assert_equal("<p>Hello.</p>", result)

class FakeDocxFile(object):
    def __init__(self, files):
        self._files = files
      
    def read(self, name):
        return self._files[name]

_SIMPLE_WORD_DOCUMENT = """<?xml version="1.0" ?>
<w:document mc:Ignorable="w14 wp14" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
  <w:body>
    <w:p w:rsidR="00E01ECE" w:rsidRDefault="000636A7">
      <w:r>
        <w:t>Hello.</w:t>
      </w:r>
      <w:bookmarkStart w:id="0" w:name="_GoBack"/>
      <w:bookmarkEnd w:id="0"/>
    </w:p>
    <w:sectPr w:rsidR="00E01ECE">
      <w:pgSz w:h="16838" w:w="11906"/>
      <w:pgMar w:bottom="1440" w:footer="708" w:gutter="0" w:header="708" w:left="1440" w:right="1440" w:top="1440"/>
      <w:cols w:space="708"/>
      <w:docGrid w:linePitch="360"/>
    </w:sectPr>
  </w:body>
</w:document>
"""
