import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!", 
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )
   
    def test_to_html_tags_paragraph(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(
            node.to_html(),
            '<p>This is a paragraph of text.</p>'
        )

    def test_to_html_without_tags(self):
        node = LeafNode(None, "I have no tags")
        self.assertEqual(
            node.to_html(),
            'I have no tags'
        )

    def test_to_html_tag_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

    def test_to_html_parent_and_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(), 
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )

    def test_to_html_with_nesting(self):
        nested_node = LeafNode("b", "nested")
        level_up_node = ParentNode("span", [nested_node])
        top_level_node = ParentNode("div", [level_up_node])
        self.assertEqual(top_level_node.to_html(), "<div><span><b>nested</b></span></div>")

if __name__ == "__main__":
    unittest.main()