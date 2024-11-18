from nodes import HTMLNode, LeafNode, ParentNode, TextNode


def main():
    dummy_text = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(dummy_text)
    dummy_html = HTMLNode(
        tag="a",
        value="Website",
        children=None,
        props={
            "href": "https://www.google.com",
            "target": "_blank",
        },
    )
    print(f"HTMLNode:\n {dummy_html}")
    print(dummy_html.props_to_html())

    dummy_leaf = LeafNode(tag="p", value="Testing", props=None)
    print(f"LeafNode:\n {dummy_leaf}")

    dummy_parent = ParentNode(tag="p", children=[dummy_leaf], props=None)
    print(f"ParentNode:\n {dummy_parent}")


if __name__ == "__main__":
    main()
