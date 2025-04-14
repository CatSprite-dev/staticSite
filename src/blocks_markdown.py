def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.split("\n\n"):
        cleaned_block = block.strip()
        if cleaned_block:
            blocks.append(cleaned_block)
    return blocks

