import shutil
import os
from markdown_utils import generate_page

def main():
    try:
        print("Clearing and updating public directory...")    
        if os.path.exists("public"):
            shutil.rmtree("public")
            shutil.copytree("static", "public")

        print("Generating page...")
        generate_page("content/index.md", "template.html", "public/index.html")

        print("Site generation complete!")
    except Exception as e:
        print(f"An error occured: {e}")

def copy_items(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        s = os.path.join(source_dir, item)
        d = os.path.join(dest_dir, item)
        if os.path.isfile(s):
            shutil.copy(s,d)
            print (f"Copied file: {s} to {d}")
        else:
            copy_items(s,d)
            print (f" Copied directory: {s} to {d}")
# Don't forget to call main() at the end of the file
main()
