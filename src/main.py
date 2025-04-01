from textnode import TextNode, TextType

def main():
    new_obj = TextNode("мой текст", TextType.BOLD, "http//:my_text")
    print(new_obj.__repr__())



main()