import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a bold text node", "bold")
        node2 = TextNode("This is a bold text node", "bold")
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a bold text node", "bold")
        node2 = TextNode("This is a bold text node", "bold", None)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a bold text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a bold text node", "bold", "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a italic text node", "italic")
        node2 = TextNode("This is a italic text node", "italic")
        self.assertEqual(node, node2)

    def test_eq5(self):
        node = TextNode("This is a italic text node", "italic")
        node2 = TextNode("This is a italic text node", "italic", None)
        self.assertEqual(node, node2)

    def test_eq6(self):
        node = TextNode("This is a italic text node", "italic", "https://www.boot.dev")
        node2 = TextNode("This is a italic text node", "italic", "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_eq7(self):
        node = TextNode("This is a code text node", "code")
        node2 = TextNode("This is a code text node", "code")
        self.assertEqual(node, node2)

    def test_eq8(self):
        node = TextNode("This is a code text node", "code")
        node2 = TextNode("This is a code text node", "code", None)
        self.assertEqual(node, node2)

    def test_eq9(self):
        node = TextNode("This is a code text node", "code", "https://www.boot.dev")
        node2 = TextNode("This is a code text node", "code", "https://www.boot.dev")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
