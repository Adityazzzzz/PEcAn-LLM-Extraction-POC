# PEcAn Project: LLM-Assisted Extraction POC (GSoC 2026)

[cite_start]This repository contains the Proof of Concept (POC) for my Google Summer of Code 2026 proposal: **Idea #5 - LLM-Assisted Extraction of Agronomic and Ecological Experiments into Structured Data** for The PEcAn Project[cite: 14, 15].

## Overview
[cite_start]This prototype demonstrates the feasibility of Layer 1 (IR Generation) of my proposed architecture[cite: 39]. [cite_start]It utilizes a multi-agent pipeline with LangChain, Pydantic, and Gemini 2.5 Flash Lite to read a complex, multi-column agronomic research paper and automatically map the unstructured text into a strict JSON format[cite: 69, 121, 122]. 

[cite_start]The output schema strictly mimics the requirements for the BETYdb `experiments` table[cite: 122, 131].

## Files Included
* [cite_start]`sample_paper.pdf`: An open-access agronomy paper ("Effect of Sowing Date on Yield and Seed Quality of Soybean") used as the ground-truth test document[cite: 164, 166].
* [cite_start]`main.py`: The extraction script containing the Curator Agent (chunking) and the Extractor Agent (structured LLM output)[cite: 40, 42]. *(Note: If you named your Python file something else, update this bullet point!)*

## Prerequisites
To run this POC locally, you will need Python installed and a Google Gemini API key.

### 1. Install Dependencies
Run the following command to install the required libraries:
```bash
pip install pydantic langchain-google-genai langchain-community pypdf
