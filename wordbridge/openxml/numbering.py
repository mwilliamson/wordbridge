# http://msdn.microsoft.com/en-us/library/office/ee922775.aspx
# The following affect only the Word UI, so can be ignored:
# w:nsid, w:multiLevelType, w:tmpl, w:tplc, w:tentative

import collections

import wordbridge.xmlparsing

def read_string(string):
    tree = wordbridge.xmlparsing.parse_string(string)
    
    abstract_definitions = dict(map(
        _read_abstract_num,
        tree.find_nodes("//w:abstractNum")
    ))
    
    return numbering(dict(
        _read_definition(abstract_definitions, element)
        for element in tree.find_nodes("//w:num")
    ))

def _read_abstract_num(element):
    abstract_num_id = element.find_value("@w:abstractNumId")
    levels = dict(map(_read_level, element.find_nodes("w:lvl")))
    return abstract_num_id, definition(levels=levels)

def _read_level(element):
    level_number = int(element.find_value("@w:ilvl"))
    start = int(element.find_value("w:start/@w:val"))
    return level_number, Level(start=start)

def _read_definition(abstract_definitions, element):
    num_id = element.find_value("@w:numId")
    abstract_num_id = element.find_value("w:abstractNumId/@w:val")
    return num_id, abstract_definitions[abstract_num_id]

Numbering = collections.namedtuple("Numbering", ["definitions"])
Definition = collections.namedtuple("Definition", ["levels"])
Level = collections.namedtuple("Level", ["start"])

numbering = Numbering
definition = Definition
level = Level
