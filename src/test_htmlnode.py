import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag="a", 
            value=None, 
            children=None, 
            props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_none_props(self):
        node = HTMLNode(
            tag="a", 
            value=None, 
            children=None, 
            props={})
        self.assertEqual(node.props_to_html(), '')
    
    def test_none_all(self):
        node = HTMLNode(
            tag=None, 
            value=None, 
            children=None, 
            props=None)
        self.assertEqual(node.props_to_html(), '')
    
    def test_to_html_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    def test_repr(self):
        node = HTMLNode(
            tag="a", 
            value=None, 
            children=None, 
            props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.__repr__(), "HTMLNode(a, None, None, {'href': 'https://www.google.com', 'target': '_blank'})")
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    
    def test_leaf_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com","target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click me!</a>')
    
    
    def test_leaf_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    

if __name__ == "__main__":
    unittest.main()