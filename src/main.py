from copy_static import *

static_path = "./static"
public_path = "./public"

def main():
    print("Deleting public directory...")
    delete_public(public_path)

    print("Copying static files to public directory...")
    generate_new_public(public_path)
    copy_static(static_path, public_path)

main()