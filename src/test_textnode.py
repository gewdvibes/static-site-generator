import unittest
from textnode import TextNode, TextType

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
                TextNode("This is a text node", TextType.NORMAL)
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

if __name__ == "__main__":
    unittest.main()
