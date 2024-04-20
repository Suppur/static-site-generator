import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "section",
            "Hello hello",
            None,
            {"class": "test", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="test" href="https://boot.dev"',
        )

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        leafnode = LeafNode(
            "p",
            "This is text",
            None,
        )
        self.assertEqual(
            leafnode.to_html(),
            '<p>This is text</p>',
        )
    def test_leaf_to_html_no_tag(self):
        leafnode = LeafNode(
            None,
            "Yo",
            {"class": "test", "href": "https://boot.dev"}
        )

class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
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
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
        )
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

        

if __name__ == "__main__":
    unittest.main()