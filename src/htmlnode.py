class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props == None:
            return ""
        attributes = ""
        for attr in self.props:
            attributes += f' {attr}="{self.props[attr]}"'
        return attributes

    def __repr__(self):
        return f'Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}'

def test():
    tag = '<a>'
    value = 'Website'
    props = {"href": "https://www.google.com", "target": "_blank",}
    node = HTMLNode(tag=tag, value=value, props=props)
    attributes = node.props_to_html()
    print(f"Attributes: {attributes}")
    print(f"Node: {node}")

test()