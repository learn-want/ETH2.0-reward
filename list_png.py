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

# Sorting function
def sort_key(item):
    # Extract file name, exclude extension and split by underscore
    segments = os.path.splitext(os.path.basename(item))[0].split('_')
    # Return the first two segments as the sort key (more can be added if needed)
    return (segments[0], segments[1] if len(segments) > 1 else '')

# Sort each category
category_1.sort(key=sort_key)
category_2.sort(key=sort_key)
category_3.sort(key=sort_key)
category_4.sort(key=sort_key)

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
    for f in sorted(category_files, key=sort_key):
        markdown_content += f"![{f}]({f})\n\n"

# Print markdown content
print(markdown_content)

with open("README.md", "w") as file:
    file.write(markdown_content)
