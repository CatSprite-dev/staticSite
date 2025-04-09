from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode



def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("Undefined text type")
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.text, "alt": text_node.url})



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