import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    split_markdown = markdown.split("\n")
    for line in split_markdown:
        if line.startswith("# "):            
            return line[1:].strip()
    raise ValueError("No title found in the markdown content")
        
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown_content = file.read()

    with open(template_path, "r") as file:
        template_content = file.read()

    try:

        title = extract_title(markdown_content)

    except ValueError:
        print(f"Warning: No title found in {from_path}. Using default.")
        title = "Untitled Page"
    
    html_content = markdown_to_html_node(markdown_content).to_html()
    template_content = template_content.replace('{{ Title }}', title)
    template_content = template_content.replace('{{ Content }}', html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(template_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    pass