from nose.tools import istest, assert_equal
from lxml import etree

from wordbridge import openxml
from wordbridge.htmlgeneration import HtmlGenerator
from wordbridge.html import HtmlBuilder

generator = HtmlGenerator()
html = HtmlBuilder()

@istest
def generating_html_for_document_concats_html_for_paragraphs():
    document = openxml.document([
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
    expected_html = html.fragment([
        html.element("p", [html.text("Hello")]),
        html.element("p", [html.text("there")])
    ])
    assert_equal(expected_html, generator.for_document(document))
