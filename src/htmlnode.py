class HTMLNode[T]:
    def __init__(self, tag: str | None = None, value: str | None = None, children: list[T] | None = None, props: dict[str, str] | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> None:
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ''
        attributes = ''
        for attr in self.props:
            attributes += f' {attr}="{self.props[attr]}"'
        return attributes

    def __repr__(self):
        return f'    Tag: {self.tag}\n    Value: {self.value}\n    Children: {self.children}\n    Props: {self.props}'
