
from unstructured.partition.pdf import partition_pdf

# Define the input PDF file path
pdf_file_path = "data/academic_paper.pdf"

# Process the PDF file
elements = partition_pdf(filename=pdf_file_path,extract_images_in_pdf=True,infer_table_structure=True,extract_image_block_types=["Image","Table"])

# Convert the elements to Markdown format
markdown_content = ""

# Process each element
for element in elements:
    if element.category == "Title":
        markdown_content += f"\n\n## {element.text}\n\n"
    elif element.category == "Image" and hasattr(element, "image_path"):
        # Include image in Markdown with a relative path
        markdown_content += f"![Image]({element.image_path})\n\n"
    elif element.category == "Table" and hasattr(element, "text"):
        # Include table text or a placeholder for tables
        markdown_content += f"\n\n{element.text}\n\n"
    elif element.text:  # Handle other text content
        markdown_content += f"{element.text}\n\n"

#Define the output Markdown file path
output_md_path = "output/unstructured/academic.md"
# Save the Markdown content to a file
with open(output_md_path, "w") as md_file:
    md_file.write(markdown_content)





