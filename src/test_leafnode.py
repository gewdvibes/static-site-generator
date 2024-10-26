import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_eq1(self):
        tag = 'a'
        value = 'Website'
        props = {"href": "https://www.google.com", "target": "_blank",}
        node = LeafNode(tag, value, props)
        attributes = node.props_to_html()
        html_string = node.to_html()

        tests = [
            (node.tag, 'a'),
            (node.value, 'Website'),
            (node.children, None),
            (node.props, {"href": "https://www.google.com", "target": "_blank",}),
            (attributes, f' href="https://www.google.com" target="_blank"'),
            (html_string, f'<a href="https://www.google.com" target="_blank">Website</a>'),
        ]

        for value, expected in tests:
            self.assertEqual(value, expected)

    def test_eq2(self):
        node = LeafNode('p', 'Cat Pics', {'href': 'https://letmegooglethat.com/?q=cats', 'autocapitalize': 'sentences'})

        tests = [
            (node.tag, 'p'),
            (node.value, 'Cat Pics'),
            (node.children, None),
            (node.props, {'href': 'https://letmegooglethat.com/?q=cats', 'autocapitalize': 'sentences'}),
            (node.props_to_html(), f' href="https://letmegooglethat.com/?q=cats" autocapitalize="sentences"'),
            (node.to_html(), f'<p href="https://letmegooglethat.com/?q=cats" autocapitalize="sentences">Cat Pics</p>'),
        ]

        for value, expected in tests:
            self.assertEqual(value, expected)

    def test_eq3(self):
        tag = 'p'
        value = None
        props = {"href": "https://www.boot.dev", "autocapitalize": "sentences",}
        node = LeafNode(tag, value, props)

        with self.assertRaises(TypeError):
            node.type_checks()

        tests = [
            (node.tag, 'p'),
            (node.value, None),
            (node.props, {"href": "https://www.boot.dev", "autocapitalize": "sentences",}),
            (node.props_to_html(), f' href="https://www.boot.dev" autocapitalize="sentences"'),
        ]

        for value, expected in tests:
            self.assertEqual(value, expected)

    def test_eq4(self):
        tag = 'p'
        value = 'Website'
        props = 52
        node = LeafNode(tag, value, props)

        with self.assertRaises(TypeError):
            node.type_checks()
            node.props_to_html()

if __name__ == "__main__":
    unittest.main()
