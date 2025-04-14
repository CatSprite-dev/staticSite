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

def split_nodes_link(old_nodes):
    new_nodes = []
    if not old_nodes:
        return []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        text = old_node.text
        links = extract_markdown_links(text)

        for link in links:
            markdown_link = f"[{link[0]}]({link[1]})"
            if markdown_link in text:
                text = text.replace(markdown_link, "&link&")
        
        sections = text.split("&")
        
        # Формирование целевого списка
        for index_section in range(0, len(sections)):
            if index_section % 2 == 0:
                split_node = TextNode(sections[index_section], TextType.TEXT)
            else:
                split_node = TextNode(links[0][0], TextType.LINK, links[0][1])
                links = links[1:]
            new_nodes.append(split_node)

        # Удаление пустых строк в начале и/или в конце    
        if new_nodes[len(new_nodes)-1].text == "":
            new_nodes.pop(len(new_nodes)-1)
        if new_nodes[0].text == "":
            new_nodes.pop(0)
    
    return new_nodes
        
def split_nodes_image(old_nodes):
    new_nodes = []
    if not old_nodes:
        return []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        text = old_node.text
        images = extract_markdown_images(text)
        
        for image in images:         
            markdown_link = f"![{image[0]}]({image[1]})"
            if markdown_link in text:
                text = text.replace(markdown_link, "&image&")
            
        sections = text.split("&")
        
        # Формирование целевого списка
        for index_section in range(0, len(sections)):
            if index_section % 2 == 0:
                split_node = TextNode(sections[index_section], TextType.TEXT)
            else:
                split_node = TextNode(images[0][0], TextType.IMAGE, images[0][1])
                images = images[1:]
            new_nodes.append(split_node)

        # Удаление пустых строк в начале и/или в конце    
        if new_nodes[len(new_nodes)-1].text == "":
            new_nodes.pop(len(new_nodes)-1)
        if new_nodes[0].text == "":
            new_nodes.pop(0)
    
    return new_nodes           

def text_to_textnodes(text):
    old_node = TextNode(text, TextType.TEXT, None)
    with_bold = split_nodes_delimiter([old_node], "**", TextType.BOLD)
    with_italic = split_nodes_delimiter(with_bold, "_", TextType.ITALIC)
    with_code = split_nodes_delimiter(with_italic, "`", TextType.CODE)
    with_images = split_nodes_image(with_code)
    with_links = split_nodes_link(with_images)
    return with_links

#node = TextNode(
#            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
#            TextType.TEXT,
#        )
#new_nodes = split_nodes_image([node])
#print(new_nodes)