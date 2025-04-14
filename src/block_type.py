from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(block):
    if "# " in block and block.count("#") < 7:
        return BlockType.HEADING
    if "```" in block and block.count("```") % 2 == 0:
        return BlockType.CODE
    if ">" in block[:1]:
        return BlockType.QUOTE
    if "- " in block[:2]:
        return BlockType.ULIST
    if ". " in block[:3] or ") " in block[:3]:
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH
    
    
print(block_to_block_type("# Headюing"))       # Должно быть BlockType.HEADING
print(block_to_block_type("- List item"))     # Должно быть BlockType.ULIST
print(block_to_block_type("```code```"))      # Должно быть BlockType.CODE
print(block_to_block_type("> Quote\n> More"))# Должно быть BlockType.QUOTE
print(block_to_block_type("Just paragraph."))





    