import unittest
from nodes import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):

    def test_eq1(self):
        tag = 'p'
        children = [
            LeafNode('a', 'Leaf1', props={"href": "https://www.boot.dev", "autocapitalize": "sentences",}),
            ParentNode(
                children=[
                    LeafNode('a', 'Leaf3', props={"href": "https://www.boot.dev"}),
                    LeafNode('p', 'Leaf4',  props={"autocapitalize": "sentences"}),
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
                tag='p'
            ),
            LeafNode('p', 'Leaf2', props={"target": "_blank"}),
        ]
        props = ''
        node = ParentNode(tag, children, props)

        print(node.to_html())

if __name__ == "__main__":
    unittest.main()

