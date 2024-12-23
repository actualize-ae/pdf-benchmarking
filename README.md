
# PDF Extraction Tools Benchmarking

This repository presents a comprehensive study and benchmarking of PDF extraction tools, focusing on their suitability for diverse document processing workflows. The evaluation covers tools' performance across various content types and metrics critical for modern AI applications like Retrieval-Augmented Generation (RAG) and intelligent agents.

## 📚 Overview

PDF extraction tools are vital for enabling AI systems to process structured and unstructured content effectively. This study evaluates six tools on their capabilities for text, table, and image extraction, OCR accuracy, Markdown conversion, and logical reading order preservation.

## ⚠️ Disclaimer

The views and feedback shared in this article are based on internal testing and evaluations conducted by Actualize's engineering team. This study does not intend to criticize, guarantee ownership, or take any responsibility for the performance or effectiveness of the tools discussed. Our aim is to transparently share the findings from our testing process without bias, providing insights for informational purposes only.

## 🧪 Tools Evaluated

The following tools were benchmarked:

- **MinerU**
- **Xerox**
- **Docling**
- **Llama Parse**
- **Marker**
- **Unstructured**

Each tool has a dedicated `main.py` file in its respective directory for running its benchmarking script.

## 📊 Key Metrics

1. Text and table extraction accuracy
2. Image clarity and positioning
3. Markdown conversion fidelity
4. OCR performance for scanned PDFs
5. Logical reading order accuracy
6. Resource utilization on CPU, MPS, and GPU platforms

## 🚀 Getting Started

### Clone the Repository

Clone the repository to your local system:

```bash
git clone https://github.com/actualize-ae/Pdf-Benchmarking.git
```

### Install Dependencies

Install the necessary dependencies for the project:

```bash
pip install -r requirements.txt
```

### Set Up MinerU

To run **MinerU**, follow these steps to create a separate Conda environment and set up its dependencies:

1. Create and activate the Conda environment:

   ```bash
   conda create -n MinerU python=3.10
   conda activate MinerU
   ```

2. Install the required dependencies for MinerU:

   ```bash
   pip install -U magic-pdf[full] --extra-index-url https://wheels.myhloli.com
   ```

3. Download and set up the necessary model files:

   - Install the Hugging Face library:
     ```bash
     pip install huggingface_hub
     ```

   - Download the model setup script:
     ```bash
     wget https://github.com/opendatalab/MinerU/raw/master/scripts/download_models_hf.py -O download_models_hf.py
     ```

   - Run the script to download the models:
     ```bash
     python download_models_hf.py
     ```

### Run Benchmarking Scripts

Run the `main.py` file for the specific tool you want to benchmark:

- For MinerU:
  ```bash
  python mineru/main.py
  ```

- For Xerox:
  ```bash
  python xerox/main.py
  ```

- For other tools, navigate to their directories and run their respective `main.py` scripts.

## 🛠 Future Work

The study highlights the need for further advancements in GPU support, table recognition, and resource optimization to enhance these tools' performance in AI-driven workflows.

## 🔗 Additional Resources

For further details about each tool, refer to their official documentation and repositories:

- [Docling](https://github.com/DS4SD/docling)
- [Llama Parse](https://docs.llamaindex.ai/en/stable/llama_cloud/llama_parse/)
- [Marker](https://github.com/VikParuchuri/marker)
- [MinerU](https://github.com/opendatalab/MinerU)
- [Unstructured](https://docs.unstructured.io/welcome)
- [Zerox](https://github.com/getomni-ai/zerox)
- [Markitdown](https://github.com/microsoft/markitdown)

