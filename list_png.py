import os

# Set the directory to be the current directory
directory = os.getcwd()

# List to store all .png files
png_files = []

# Walk through directory
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in [f for f in filenames if f.endswith(".png")]:
        # Get the relative file path
        relative_path = os.path.relpath(os.path.join(dirpath, filename), directory)
        png_files.append(relative_path)

files = png_files

# Categorize the figures
category_1 = [f for f in files if f.endswith("_proposer.png")]
category_2 = [f for f in files if f.endswith("_attester.png")]
category_3 = [f for f in files if f.endswith("_sync.png")]
category_4 = [f for f in files if not any(f.endswith(suffix) for suffix in ["_proposer.png", "_attester.png", "_sync.png"])]

# Generate markdown
markdown_content = ""

categories = [
    ("Category 1: Proposer", category_1),
    ("Category 2: Attester", category_2),
    ("Category 3: Sync", category_3),
    ("Category 4: Others", category_4)
]

for title, category_files in categories:
    markdown_content += f"## {title}\n"
    for f in category_files:
        markdown_content += f"![{f}]({f})\n\n"

# Print markdown content
print(markdown_content)
