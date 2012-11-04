from nose.tools import istest, assert_equal

from wordbridge.openxml import numbering
from wordbridge import openxml

@istest
def numbering_instance_is_read_from_num_element_with_abstract_num_base():
    numbering_xml = _create_numbering_xml("""
  <w:abstractNum w:abstractNumId="0">
    <w:lvl w:ilvl="0">
      <w:start w:val="1"/>
      <w:numFmt w:val="bullet"/>
      <w:lvlText w:val="o"/>
    </w:lvl>
    <w:lvl w:ilvl="1">
      <w:start w:val="2"/>
      <w:numFmt w:val="bullet"/>
      <w:lvlText w:val="o"/>
    </w:lvl>
  </w:abstractNum>
  <w:num w:numId="1">
    <w:abstractNumId w:val="0"/>
  </w:num>
""")
    
    result = numbering.read_string(numbering_xml)
    
    expected_numbering = numbering.numbering({
        "1": numbering.definition(levels={
            0: numbering.level(start=1),
            1: numbering.level(start=2)
        })
    })
    assert_equal(expected_numbering, result)

def _create_numbering_xml(inner_xml):
    return _NUMBERING_TEMPLATE.format(inner_xml)
    
_NUMBERING_TEMPLATE = """<?xml version="1.0" ?>
<w:numbering mc:Ignorable="w14 wp14" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
  {0}
</w:numbering>
"""
