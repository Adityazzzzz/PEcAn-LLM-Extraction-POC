# PEcAn Project: LLM-Assisted Extraction POC (GSoC 2026)

This repository contains the Proof of Concept (POC) for my Google Summer of Code 2026 proposal: **Idea #5 - LLM-Assisted Extraction of Agronomic and Ecological Experiments into Structured Data** for The PEcAn Project.

## Overview
This prototype demonstrates the feasibility of Layer 1 (IR Generation) of my proposed architecture.It utilizes a multi-agent pipeline with LangChain, Pydantic, and Gemini 2.5 Flash Lite to read a complex, multi-column agronomic research paper and automatically map the unstructured text into a strict JSON format. 

The output schema strictly mimics the requirements for the BETYdb `experiments` table.

## Files Included
* `sample_paper.pdf`: An open-access agronomy paper ("Effect of Sowing Date on Yield and Seed Quality of Soybean") used as the ground-truth test document.
* `main.py`: The extraction script containing the Curator Agent (chunking) and the Extractor Agent (structured LLM output). *(Note: If you named your Python file something else, update this bullet point!)*

## Prerequisites
To run this POC locally, you will need Python installed and a Google Gemini API key.

### 1. Install Dependencies
Run the following command to install the required libraries:
```bash
pip install pydantic langchain-google-genai langchain-community pypdf   
```

### 2. Set API Key
You must expose your Gemini API key as an environment variable before running the script.
Mac/Linux:
```bash
export GEMINI_API_KEY="your_api_key_here"   
```
Windows (Command Prompt):
```bash
set GEMINI_API_KEY="your_api_key_here"
```
Running the Extractor
Simply execute the Python script in your terminal:

```bash
python main.py
```

## How it Works under the Hood
* Document Loading: PyPDFLoader reads the multi-column layout of the PDF.
* Context Chunking: The script isolates the first few pages (Abstract + Materials & Methods) to reduce context window noise and improve extraction accuracy.
* Structured Extraction: Using LangChain's .with_structured_output(), the LLM is forced to return data strictly conforming to the BETYdbExperimentIR Pydantic class.


## Expected Output
The script will output a validated JSON object containing the extracted metadata, formatted perfectly for the Intermediate Representation (IR) laye
```bash
{
  "name": "Effect of Sowing Date on Yield and Seed Quality of Soybean",
  "start_date": "2013-11-18",
  "end_date": "2014-03-08",
  "description": "A field experiment was conducted to study...",
  "design": "Randomized Complete Block Design (RCBD) factorial"
}
```


***
