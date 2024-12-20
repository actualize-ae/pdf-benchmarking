from llama_parse import LlamaParse

# Initialize the LlamaParse parser
parser = LlamaParse(
    api_key="your-api-key",  # can also be set in your env as LLAMA_CLOUD_API_KEY
    result_type="markdown",  # "markdown" and "text" are available
    verbose=True,parsing_instruction="Extract the text from the PDF and format it as Markdown, preserving headings, lists, code blocks, images and non-text elements.",
    is_formatting_instruction=False
)

# # Define parsing instructions for a document
# parsing_instruction = """
# Extract the text from the PDF and format it as Markdown, preserving headings, lists, code blocks, images and non-text elements.
# """

# Parse the document
parsed_documents = parser.load_data("data/academic_paper.pdf")

# Save the parsed results
with open('output/llama_parse/academic.md', 'w') as f:
    for doc in parsed_documents:
        f.write(doc.text + '\n')