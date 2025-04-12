import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if not old_nodes:
        return []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        text = old_node.text
       
        # Проверка наличия закрывающего делителя
        if text.count(delimiter) % 2 != 0:
            raise Exception("Invalid markdown syntax: mismatched delimiter")
        
        sections = text.split(delimiter)

        # Формирование целевого списка
        for index_of_section in range(0, len(sections)):
            if index_of_section % 2 == 0:
                split_node = TextNode(sections[index_of_section], TextType.TEXT)
            else:
                split_node = TextNode(sections[index_of_section], text_type)
            new_nodes.append(split_node)

        # Удаление пустых строк в начале и/или в конце    
        if new_nodes[len(new_nodes)-1].text == "":
            new_nodes.pop(len(new_nodes)-1)
        if new_nodes[0].text == "":
            new_nodes.pop(0)
    
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches
