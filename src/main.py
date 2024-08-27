import shutil
import os
from textnode import TextNode

def main():
    # Create a TextNode object
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    
    copy_items("static", "public")
    # Print the object
    print(node)

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
