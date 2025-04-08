from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    textnode_obj = TextNode("мой текст", TextType.BOLD, "http//:my_text")

    htmlnode_obj = HTMLNode(
            tag="a", 
            value="My text is this", 
            children= [LeafNode("b", "Bold text")], 
            props={"href": "https://www.google.com", "target": "_blank"})
    
    parentnode_obj = ParentNode("p", 
            children=[
                LeafNode("b", "Bold text"), 
                LeafNode(None, "Normal text"), 
                LeafNode("i", "italic text"), 
                LeafNode(None, "Normal text")
                ],
            )
    
    leafnode_obj = LeafNode("p", "My text is this")
    print(f"1. {textnode_obj.__repr__()}")
    print(f"2. {htmlnode_obj.__repr__()}")
    print(f"3. {leafnode_obj.__repr__()}")
    print(f"4. {parentnode_obj.__repr__()}")
    print(f"5: {parentnode_obj.to_html()}")

main()