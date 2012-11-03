from nose.tools import istest, assert_equal
from lxml import etree

from wordbridge import openxml
from wordbridge.htmlgeneration import HtmlGenerator
from wordbridge.html import HtmlBuilder
from wordbridge import styles

html = HtmlBuilder()

@istest
def generating_html_for_document_concats_html_for_paragraphs():
    document = openxml.document([
        _paragraph_of_text("Hello"),
        _paragraph_of_text("there")
    ])
    expected_html = html.fragment([
        html.element("p", [html.text("Hello")]),
        html.element("p", [html.text("there")])
    ])
    
    generator = HtmlGenerator()
    assert_equal(expected_html, generator.html_for_document(document))

@istest
def html_for_paragraph_uses_p_tag_if_there_is_no_style():
    paragraph = _paragraph_of_text("Hello")
    expected_html = html.fragment([
        html.element("p", [html.text("Hello")])
    ])
    
    generator = HtmlGenerator()
    assert_equal(expected_html, generator.html_for_paragraph(paragraph))

@istest
def style_mapping_is_used_to_generate_html_for_paragraph_with_style():
    paragraph = _paragraph_of_text("Hello", style="Heading1")
    expected_html = html.fragment([
        html.element("h1", [html.text("Hello")])
    ])
    
    generator = HtmlGenerator(paragraph_styles=[
        styles.map_word_style("Heading1").to(styles.top_level_element("h1"))
    ])
    assert_equal(expected_html, generator.html_for_paragraph(paragraph))
    
@istest
def consecutive_word_bullet_paragraphs_are_converted_to_single_html_list():
    document = openxml.document([
        _paragraph_of_text("Apples", style="Bullet1"),
        _paragraph_of_text("Bananas", style="Bullet1")
    ])
    expected_html = html.fragment([
        html.element("ul", [
            html.element("li", [html.text("Apples")]),
            html.element("li", [html.text("Bananas")])
        ])
    ])
    
    generator = HtmlGenerator(paragraph_styles=[
        styles.map_word_style("Bullet1").to(styles.unordered_list())
    ])
    assert_equal(expected_html, generator.html_for_document(document))


@istest
def bullets_of_multiple_depth_are_converted_to_nested_lists():
    document = openxml.document([
        _paragraph_of_text("Food", style="Bullet1"),
        _paragraph_of_text("Apples", style="Bullet2"),
        _paragraph_of_text("Bananas", style="Bullet2"),
        _paragraph_of_text("Drinks", style="Bullet1"),
    ])
    expected_html = html.fragment([
        html.element("ul", [
            html.element("li", [
                html.text("Food"),
                html.element("ul", [
                    html.element("li", [html.text("Apples")]),
                    html.element("li", [html.text("Bananas")])
                ])
            ]),
            html.element("li", [html.text("Drinks")])
        ])
    ])
    
    generator = HtmlGenerator(paragraph_styles=[
        styles.map_word_style("Bullet1").to(styles.unordered_list(depth=1)),
        styles.map_word_style("Bullet2").to(styles.unordered_list(depth=2))
    ])
    assert_equal(expected_html, generator.html_for_document(document))

def _paragraph_of_text(text, style=None):
    return openxml.paragraph([_run_of_text(text)], style=style)

def _run_of_text(text):
    return openxml.run([openxml.text(text)])
