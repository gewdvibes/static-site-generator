from enum import Enum

class TextType(Enum):
    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        if (self.text == node.text and self.text_type == node.text_type and self.url == node.url):
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

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
            return ''
        attributes = ''
        for attr in self.props:
            attributes += f' {attr}="{self.props[attr]}"'
        return attributes

    def __repr__(self):
        return (
            f'\n    Tag: {self.tag}\n'
            f'    Value: {self.value}\n'
            f'    Children: {self.children}\n'
            f'    Props: {self.props}\n'
        )

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError('Value is required')
        if self.tag is None or self.tag.strip() == "":
            return f'{self.value}'
        return (
            f'<{self.tag}'
            f'{self.props_to_html()}'
            f'>{self.value}</{self.tag}>'
        )

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None or self.tag.strip() == "":
            raise ValueError('Tag is required')
        if self.children is None or type(self.children) is not type([]):
            raise ValueError('Children are required and must be a list')

        children_string = ''
        for child in self.children:
            children_string += child.to_html()

        return f'<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>'

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag='b', value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag='i', value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag='code', value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag='a', value=text_node.text, props={'href': text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag='img', value='', props={'src': text_node.url, 'alt': text_node.text})
        case _:
            raise Exception('Not a valid type.')

