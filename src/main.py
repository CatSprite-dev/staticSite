from generate_page import generate_page, generate_pages_recursive
from copy_static import *

content_path = "./content"
template_path = "template.html"
static_path = "./static"
public_path = "./public"

def main():
    print("Deleting public directory...")
    delete_public(public_path)

    print("Copying static files to public directory...")
    generate_new_public(public_path)
    copy_static(static_path, public_path)
    generate_pages_recursive(content_path, template_path, public_path)

main()