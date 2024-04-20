class HTMLNode:
    def __init__(self, tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        str_prop = ""
        for item in self.props:
            str_prop += f' {item}="{self.props[item]}"'
        return str_prop
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Error: Value required")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    str_nested_nodes = ""
    def to_html(self):
        if self.tag is None:
            raise ValueError("Error: tag is required")
        if not self.children:
            raise ValueError("Error: Node has no children")
        
        def recurse_children(children):
            if not children:
                return ""
            return children[0].to_html() + recurse_children(children[1:])
        
        return f"<{self.tag}{self.props_to_html()}>{recurse_children(self.children)}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"