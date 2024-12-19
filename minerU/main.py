# from docling.document_converter import DocumentConverter

# source = "data/basic-md-julia.pdf" 
# converter = DocumentConverter()
# result = converter.convert(source)
# result.document.export_to_markdown()
import subprocess

def run_minerU_script():
    # Run the external command for PDF processing
    command = ["magic-pdf","-p" "data/academic_paper.pdf", "-o", "output/minerU"]
    process = subprocess.run(command, capture_output=True, text=True)
    return process.returncode, process.stdout, process.stderr

# Run the external script
return_code, stdout, stderr = run_minerU_script()

# Output command results
print("\nCommand Output:")
print(stdout)
print("\nCommand Errors (if any):")
print(stderr)