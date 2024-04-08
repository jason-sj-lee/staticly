import unittest

from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode
)

class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode("p", "hello world")
        html = node.props_to_html()
        self.assertEqual(html, "")

    def test_one_prop(self):
        node = HTMLNode("p", "hello world", None, {"href": "https://www.google.com"})
        html = node.props_to_html()
        self.assertEqual(html, ' href="https://www.google.com"')

    def test_two_props(self):
        node = HTMLNode("p", "hello world", None, {"href": "https://www.google.com", "target": "_blank"})
        html = node.props_to_html()
        self.assertEqual(html, ' href="https://www.google.com" target="_blank"')

    def test_leaf_node(self):
        leaf_node = LeafNode("p", "hello world", None)
        html = leaf_node.to_html()
        self.assertEqual(html, "<p>hello world</p>")

    def test_leaf_node2(self):
        leaf_node = LeafNode("a", "boot dev", {"href": "https://boot.dev"})
        html = leaf_node.to_html()
        self.assertEqual(html, '<a href="https://boot.dev">boot dev</a>')
    
    def test_to_html_with_children(self):
        leaf_node = LeafNode("p", "hello world")
        parent_node = ParentNode("div", [leaf_node])
        self.assertEqual(parent_node.to_html(), '<div><p>hello world</p></div>')
    
    def test_to_html_with_grandchildren(self):
        grandchild = LeafNode("b", "hello world")
        child = ParentNode("p", [grandchild])
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), '<div><p><b>hello world</b></p></div>')

if __name__ == "__main__":
    unittest.main()
