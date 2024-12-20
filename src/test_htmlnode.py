import unittest
from nodes import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq1(self):
        tag = "a"
        value = "Website"
        children = None
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(tag, value, children, props)

        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )

        self.assertNotEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_eq2(self):
        node = HTMLNode()

        self.assertEqual(node.props_to_html(), "")

        self.assertNotEqual(node.props_to_html(), ' href="https://www.google.com"')

        tests = [
            (node.tag, None),
            (node.value, None),
            (node.children, None),
            (node.props, None),
        ]

        for value, expected in tests:
            self.assertEqual(value, expected)

    def test_eq3(self):
        tag = "a"
        value = "Cat Pics"
        children = None
        props = {
            "href": "https://www.boot.dev",
            "autocapitalize": "sentences",
        }
        node = HTMLNode(tag, value, children, props)

        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.boot.dev" autocapitalize="sentences"',
        )

        self.assertNotEqual(node.props_to_html(), ' autocapitalize="sentences"')

        self.assertNotEqual(
            node.props_to_html(),
            'href="https://www.boot.dev" autocapitalize="sentences"',
        )

        self.assertEqual(node.children, children)


if __name__ == "__main__":
    unittest.main()
