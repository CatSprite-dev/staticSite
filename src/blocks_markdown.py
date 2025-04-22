from enum import Enum
from htmlnode import *
from textnode import *
from inline_markdown import *

def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.split("\n\n"):
        cleaned_block = block.strip()
        if cleaned_block:
            blocks.append(cleaned_block)
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if "1. " in block[:3] or "1) " in block[:3]:
        i = 1
        for line in lines:
            if line.startswith(f"{i}. ") or line.startswith(f"{i}) "):
                i += 1
                return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_node = ParentNode("div", [], None)
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            child_node = ParentNode("p", [], None)
            inlines = text_to_textnodes(" ".join(block.split("\n")))
            for inline in inlines:
                html_node = text_node_to_html_node(inline)
                child_node.children.append(html_node)
            parent_node.children.append(child_node)

        if block_type == BlockType.QUOTE:
            child_node = ParentNode("blockquote", [], None)
            lines = block.split("\n")
            for line in lines:
                if lines.index(line) == len(lines) - 1:
                    text_nodes = text_to_textnodes(line.lstrip(">"))
                else:
                    text_nodes = text_to_textnodes(line.lstrip("> "))
                for text_node in text_nodes:
                    html_node = text_node_to_html_node(text_node)
                    child_node.children.append(html_node)
            parent_node.children.append(child_node)

        if block_type == BlockType.ULIST:
            child_node = ParentNode("ul", [], None)
            items = block.split("\n")
            for item in items:
                if item != "":
                    text_nodes = text_to_textnodes(item[2:])
                    for text_node in text_nodes:
                        new_item = text_node_to_html_node(text_node)
                child_node.children.append(ParentNode("li", [new_item]))
            parent_node.children.append(child_node)

        if block_type == BlockType.OLIST:
            child_node = ParentNode("ol", [], None)
            items = block.split("\n")
            for item in items:
                if item != "":
                    text_nodes = text_to_textnodes(item[3:])
                    for text_node in text_nodes:
                        new_item = text_node_to_html_node(text_node)
                child_node.children.append(ParentNode("li", [new_item]))
            parent_node.children.append(child_node)
        
        if block_type == BlockType.CODE:
            child_node = ParentNode("code", [], None)
            text = block.strip("```").lstrip()
            x = TextNode(text, TextType.TEXT)
            new_item = text_node_to_html_node(x)
            child_node.children.append(new_item)
            pre_tag = ParentNode("pre", [child_node])
            parent_node.children.append(pre_tag)

        if block_type == BlockType.HEADING:
            lines = block.split("\n")
            for line in lines:
                parent_node.children.append(text_to_children(line))

            
    return parent_node
    
def text_to_children(text):
    count = text.count("#")
    if count == 1:
        child_node = ParentNode("h1", [])
        text_nodes = text_to_textnodes(text[2:])
        for text_node in text_nodes:
            child_node.children.append(text_node_to_html_node(text_node))
        return child_node
    if count == 2:
        child_node = ParentNode("h2", [])
        text_nodes = text_to_textnodes(text[3:])
        for text_node in text_nodes:
            child_node.children.append(text_node_to_html_node(text_node))
        return child_node
    if count == 3:
        child_node = ParentNode("h3", [])
        text_nodes = text_to_textnodes(text[4:])
        for text_node in text_nodes:
            child_node.children.append(text_node_to_html_node(text_node))
        return child_node
    if count == 4:
        child_node = ParentNode("h4", [])
        text_nodes = text_to_textnodes(text[5:])
        for text_node in text_nodes:
            child_node.children.append(text_node_to_html_node(text_node))
        return child_node
    if count == 5:
        child_node = ParentNode("h5", [])
        text_nodes = text_to_textnodes(text[6:])
        for text_node in text_nodes:
            child_node.children.append(text_node_to_html_node(text_node))
        return child_node
    if count == 6:
        child_node = ParentNode("h6", [])
        text_nodes = text_to_textnodes(text[7:])
        for text_node in text_nodes:
            child_node.children.append(text_node_to_html_node(text_node))
        return child_node

