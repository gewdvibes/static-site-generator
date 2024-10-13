import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq1(self):
        tag = 'a'
        value = 'Website'
        children = None
        props = {"href": "https://www.google.com", "target": "_blank",}
        node = HTMLNode(tag=tag, value=value, children=children, props=props)
        attributes = node.props_to_html()
        print(f"Attributes: {attributes}")
        print(f"Node: \n{node}")

    def test_eq2(self):
        node = HTMLNode()
        attributes = node.props_to_html()
        print(f"Attributes: {attributes}")
        print(f"Node: \n{node}")

    def test_eq3(self):
        tag = 'p'
        children = [HTMLNode('a','website',None,None), HTMLNode('h1','header',None,None), HTMLNode('p','paragraph',None,None)]
        props = {"href": "https://www.boot.dev", "autocapitalize": "sentences",}
        node = HTMLNode(tag=tag, children=children, props=props)
        attributes = node.props_to_html()
        self.assertEqual(node.tag, tag)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, props)
        self.assertEqual(attributes, f' href="https://www.boot.dev" autocapitalize="sentences"')
        print(f"Attributes: {attributes}")
        print(f"Node: \n{node}")
if __name__ == "__main__":
    unittest.main()
