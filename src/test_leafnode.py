import unittest
from nodes import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq1(self):
        tag = "a"
        value = "Website"
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = LeafNode(tag, value, props=props)
        attributes = node.props_to_html()
        html_string = node.to_html()

        tests = [
            (node.children, None),
            (attributes, ' href="https://www.google.com" target="_blank"'),
            (
                html_string,
                '<a href="https://www.google.com" target="_blank">Website</a>',
            ),
        ]

        for value, expected in tests:
            self.assertEqual(value, expected)

    def test_eq2(self):
        tag = "p"
        value = "Cat Pics"
        props = {
            "href": "https://letmegooglethat.com/?q=cats",
            "autocapitalize": "sentences",
        }
        node = LeafNode(tag, value, props)

        tests = [
            (node.children, None),
            (
                node.props_to_html(),
                ' href="https://letmegooglethat.com/?q=cats" autocapitalize="sentences"',
            ),
            (
                node.to_html(),
                '<p href="https://letmegooglethat.com/?q=cats" autocapitalize="sentences">Cat Pics</p>',
            ),
        ]

        for value, expected in tests:
            self.assertEqual(value, expected)

    def test_eq3(self):
        tag = "p"
        value = None
        props = {
            "href": "https://www.boot.dev",
            "autocapitalize": "sentences",
        }
        node = LeafNode(tag, value, props)

        tests = [
            (node.value, None),
            (node.children, None),
            (
                node.props_to_html(),
                ' href="https://www.boot.dev" autocapitalize="sentences"',
            ),
        ]

        for value, expected in tests:
            self.assertEqual(value, expected)

        with self.assertRaises(ValueError):
            node.to_html()

    def test_eq4(self):
        tag = "p"
        value = "Website"
        props = 52
        node = LeafNode(tag, value, props)

        with self.assertRaises(TypeError):
            node.props_to_html()


if __name__ == "__main__":
    unittest.main()
