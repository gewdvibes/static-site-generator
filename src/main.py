from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode

def main():
    dummy = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(dummy)
    dummy_html = HTMLNode(
        tag = 'a',
        value = 'Website',
        children = None,
        props = {"href": "https://www.google.com", "target": "_blank",}
    )
    print(f'HTMLNode:\n {dummy_html}')

    dummy_leaf = LeafNode(
        tag = 'p',
        value = 'Testing',
        props = None
    )
    print(f'LeafNode:\n {dummy_leaf}')

    dummy_parent = LeafNode(
        tag = 'p',
        value = 'Testing',
        props = None
    )
    print(f'ParentNode:\n {dummy_parent}')

if __name__ == "__main__":
    main()
