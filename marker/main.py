import subprocess

def run_marker_script():
    # Run the external command for PDF processing
    command = ["marker_single", "data/academic_paper.pdf","--output_dir", "output/marker"]
    process = subprocess.run(command, capture_output=True, text=True)
    return process.returncode, process.stdout, process.stderr

# Run the external script
return_code, stdout, stderr = run_marker_script()

# Output command results
print("\nCommand Output:")
print(stdout)
print("\nCommand Errors (if any):")
print(stderr)