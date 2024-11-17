import unittest
from nodes import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_equality(self):
        tests = [
            (
                TextNode("This is a text node", "bold"),
                TextNode("This is a text node", "bold"),
            ),
            (
                TextNode("This is a text node", "italic"),
                TextNode("This is a text node", "italic", None),
            ),
            (
                TextNode("This is a text node", "link", "https://www.boot.dev"),
                TextNode("This is a text node", "link", "https://www.boot.dev"),
            ),
            (
                TextNode("This is a text node", "code"),
                TextNode("This is a text node", "code"),
            ),
            (
                TextNode("This is a text node", "image", "https://www.boot.dev"),
                TextNode("This is a text node", "image", "https://www.boot.dev"),
            ),
        ]

        for value, expected in tests:
            self.assertEqual(value, expected)

    def test_inequality(self):
        tests = [
            (
                TextNode("This is a text node", "italic"),
                TextNode("This is a text node", "text"),
            ),
            (
                TextNode("This is a text node", "code", "https://www.boot.dev"),
                TextNode("This is a text node", "code"),
            ),
            (
                TextNode("This is a text node", "bold"),
                TextNode("This is a text node", "code"),
            ),
            (
                TextNode("This is a text node", "bold", "https://www.boot.dev"),
                TextNode("This is a text node", "bold", "https://www.google.com"),
            ),
        ]

        for value, expected in tests:
            self.assertNotEqual(value, expected)

    def test_enum_validity(self):
        tests = [
            "random",
            "test",
            "notachoice",
            "foo",
            "bar",
            "foobar",
            "bolt",
        ]

        with self.assertRaises(ValueError):
            for test in tests:
                TextNode("This is a text node", f"{test}", "https://www.google.com")

    def test_conversion(self):
        tests = [
            (TextNode("testing", "text"), "testing"),
            (TextNode("testing", "bold"), "<b>testing</b>"),
            (TextNode("testing", "italic"), "<i>testing</i>"),
            (TextNode("testing", "code"), "<code>testing</code>"),
            (
                TextNode("testing", "link", "https://www.boot.dev"),
                '<a href="https://www.boot.dev">testing</a>',
            ),
            (
                TextNode("testing", "image", "https://www.google.com/image.jpg"),
                '<img src="https://www.google.com/image.jpg" alt="testing"></img>',
            ),
        ]

        for value, expected in tests:
            leaf = text_node_to_html_node(value)
            self.assertEqual(leaf.to_html(), expected)


if __name__ == "__main__":
    unittest.main()
