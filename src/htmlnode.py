class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        attributes = ""
        for attr in self.props:
            attributes += f' {attr}="{self.props[attr]}"'
        return attributes

    def __repr__(self):
        return f'    Tag: {self.tag}\n    Value: {self.value}\n    Children: {self.children}\n    Props: {self.props}'
