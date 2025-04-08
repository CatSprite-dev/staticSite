class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        props_html = ""
        if self.props != {} and self.props != None:
            for key, value in self.props.items():
                props_html += f' {key}="{value}"'
            return props_html
        return props_html
        
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("Error: No value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LEAFNode({self.tag}, {self.value}, {self.props})"
    
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Error: No tag")
        if self.children is None:
            raise ValueError("Error: No children")
    
        def child_to_html(children):
            if len(children) == 0:
                return ""
            leafnode = children[0]
            return leafnode.to_html() + child_to_html(children[1:])   
        
        return f"<{self.tag}>{child_to_html(self.children)}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"