class HTMLNode:
    def __init__(
        self,
        tag = None,
        value = None,
        children = None,
        props = None
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ''
        attributes = ''
        for attr in self.props:
            attributes += f' {attr}="{self.props[attr]}"'
        return attributes

    def __repr__(self):
        return (
            f'    Tag: {self.tag}\n'
            f'    Value: {self.value}\n'
            f'    Children: {self.children}\n'
            f'    Props: {self.props}'
        )

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError('Value is required')
        if self.tag == None or self.value == "":
            return f'{self.value}'
        return (
            f'<{self.tag}'
            f'{self.props_to_html()}'
            f'>{self.value}</{self.tag}>'
        )

    def type_checks(self):
        if type(self.value) is type(None):
            raise TypeError('Value cannot be None')
        if type(self.children) is not type(None):
            raise TypeError('LeafNodes cannot have children')
        if type(self.props) is not type({}) or type(self.props) is not type(None):
            raise TypeError('Props must be a dictionary or None')

class ParentNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, value, children, props)
