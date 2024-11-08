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

        self.assertEqual(node.to_html(), '<p><a href="https://www.boot.dev" autocapitalize="sentences">Leaf1</a><p><a href="https://www.boot.dev">Leaf3</a><p autocapitalize="sentences">Leaf4</p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p target="_blank">Leaf2</p></p>')

if __name__ == "__main__":
    unittest.main()

