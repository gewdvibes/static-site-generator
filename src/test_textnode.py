import unittest
from nodes import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_equality(self):
        tests = [
            (
                TextNode("This is a text node", TextType.BOLD),
                TextNode("This is a text node", TextType.BOLD)
            ),
            (
                TextNode("This is a text node", TextType.ITALIC),
                TextNode("This is a text node", TextType.ITALIC, None)
            ),
            (
                TextNode("This is a text node", TextType.LINK, "https://www.boot.dev"),
                TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
            ),
            (
                TextNode("This is a text node", TextType.CODE),
                TextNode("This is a text node", TextType.CODE)
            ),
            (
                TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev"),
                TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev")
            ),
        ]

        for value, expected in tests:
            self.assertEqual(value, expected)

    def test_inequality(self):
        tests = [
            (
                TextNode("This is a text node", TextType.ITALIC),
                TextNode("This is a text node", TextType.TEXT)
            ),
            (
                TextNode("This is a text node", TextType.CODE, "https://www.boot.dev"),
                TextNode("This is a text node", TextType.CODE)
            ),
            (
                TextNode("This is a text node", TextType.BOLD),
                TextNode("This is a text node", TextType.CODE)
            ),
            (
                TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev"),
                TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
            ),
        ]

        for value, expected in tests:
            self.assertNotEqual(value, expected)

    def test_conversion(self):
        tests = [
            TextNode("testing", TextType.TEXT),
            TextNode("testing", TextType.BOLD),
            TextNode("testing", TextType.ITALIC),
            TextNode("testing", TextType.CODE),
            TextNode("testing", TextType.LINK, "https://www.boot.dev"),
            TextNode("testing", TextType.IMAGE, "https://www.google.com/image.jpg"),
        ]

        for node in tests:
            leaf = text_node_to_html_node(node)
            print(leaf.to_html())

if __name__ == "__main__":
    unittest.main()
