import unittest

from textnode import TextNode, TextType
from main import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_different_text(self):
        node = TextNode("This is a text", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_different_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_with_url(self):
        node = TextNode("This is a text node", TextType.LINK, url="https://example.com")
        node2 = TextNode("This is a text node", TextType.LINK, url="https://different.com")
        self.assertNotEqual(node, node2)
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        image_url = "https://example.com/image.jpg"
        alt_text = "Example image"
        node = TextNode(image_url, TextType.IMAGE, alt_text)
        
        html_node = text_node_to_html_node(node)
    
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(len(html_node.props), 2)
        self.assertEqual(html_node.props["src"], image_url)
        self.assertEqual(html_node.props["alt"], alt_text)
    
    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "https://example.com/image.jpg")

        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(len(html_node.props), 1)
        self.assertEqual(html_node.props["href"], "https://example.com/image.jpg")


if __name__ == "__main__":
    unittest.main()