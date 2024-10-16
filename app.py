import os

def create_index_html(directory):
    index_path = os.path.join(directory, "index.html")
    
    with open(index_path, "w", encoding="utf-8") as index_file:
        index_file.write("<html><head><title>CHM Content Index</title></head><body>\n")
        index_file.write("<h1>CHM File Content Index</h1>\n")
        index_file.write("<ul>\n")

        # Iterate through all files and directories in `ac-chm` to build links
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".html") and file != "index.html":
                    # Generate a relative path and create a link
                    rel_path = os.path.relpath(os.path.join(root, file), directory)
                    index_file.write(f'<li><a href="{rel_path}">{rel_path}</a></li>\n')

        index_file.write("</ul>\n</body></html>")
    
    print(f"Index file created at {index_path}")

# Path to your `ac-chm` directory
directory = "."
create_index_html(directory)
