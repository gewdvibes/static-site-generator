from htmlnode import HTMLNode
from textnode import TextNode

def main():
    dummy = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(dummy)
    dummy_html = HTMLNode(tag='a', value='Website', children=None, props={"href": "https://www.google.com", "target": "_blank",})
    print(dummy_html)
if __name__ == "__main__":
    main()
