import os
from blocks_markdown import *
from copy_static import copy_static

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING:
            lines = block.split("\n")
            for line in lines:
                if line.startswith("#"):
                    return line.strip("#").strip()
        raise Exception("No title")
    
def generate_page(md_file_path, template_path, dest_path, basepath):
    print(f"Generating page from {md_file_path} to {dest_path} using {template_path}")
    #file_list = os.listdir(from_path)
    #for file in file_list:
        #if ".md" in file:
    #file_path = os.path.join(from_path, file)
    with open(md_file_path) as md:
        content = md.read()
    with open(template_path) as html:
        template = html.read()
    
    html_content = markdown_to_html_node(content).to_html()
    title = extract_title(content)
    full_html_content = template.replace("{{ Title }}", title)
    full_html_content = full_html_content.replace("{{ Content }}", html_content)
    full_html_content = full_html_content.replace('href="/', f'href="{basepath}')
    full_html_content = full_html_content.replace('src="/', f'src="{basepath}')


    file_out = open(os.path.join(dest_path, "index.html"), "w")
    file_out.write(full_html_content)
    file_out.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    file_list = os.listdir(dir_path_content)
    for file in file_list:
        if os.path.isfile(os.path.join(dir_path_content, file)):
            file_path = os.path.join(dir_path_content, file)
            public_path = os.path.dirname(os.path.join(dest_dir_path, file))
            generate_page(file_path, template_path, public_path, basepath)
        else:
            copy_static(dir_path_content, dest_dir_path)
            new_src_path = os.path.join(dir_path_content, file)
            new_dest_path = os.path.join(dest_dir_path, file)
            generate_pages_recursive(new_src_path, template_path, new_dest_path, basepath)

        