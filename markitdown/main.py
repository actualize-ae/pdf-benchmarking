import subprocess

def run_markitdown_script():
    # Correctly handle file output in subprocess
    input_file = "data/academic_paper.pdf"
    output_file = "output/markitdown/academic.md"
    
    with open(output_file, "w") as outfile:
        # Run the command and redirect stdout to the file
        process = subprocess.run(
            ["markitdown", input_file],
            stdout=outfile,
            stderr=subprocess.PIPE,
            text=True
        )
    return process.returncode, process.stderr

# Run the external script
return_code, stderr = run_markitdown_script()

# Output command results
print("\nCommand Errors (if any):")
print(stderr)
