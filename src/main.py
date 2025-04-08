from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    new_textnode_obj = TextNode("мой текст", TextType.BOLD, "http//:my_text")
    print(new_textnode_obj.__repr__())
    new_htmlnode_obj = HTMLNode(
            tag="a", 
            value=None, 
            children=None, 
            props={"href": "https://www.google.com", "target": "_blank"})
    print(new_htmlnode_obj.__repr__())




main()