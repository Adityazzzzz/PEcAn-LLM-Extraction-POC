import os
from pydantic import BaseModel, Field
from typing import Optional
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader

# 1. Define the Pydantic Schema (Mapping to BETYdb 'experiments' table)
class BETYdbExperimentIR(BaseModel):
    name: str = Field(description="The official title of the agronomic experiment.")
    start_date: str = Field(description="Start date of the experiment in strict YYYY-MM-DD format.")
    end_date: Optional[str] = Field(description="End date in strict YYYY-MM-DD format.")
    description: str = Field(description="Summary of goals, methods, and crop types.")
    design: str = Field(description="Statistical design (e.g., randomized complete block).")

# 2. Document Loading & Curator Agent (Semantic Chunking)
pdf_filename = "sample_paper.pdf"
loader = PyPDFLoader(pdf_filename)
pages = loader.load()

# Isolate early pages (Abstract + Materials & Methods) to reduce context noise
pages_to_scan = min(4, len(pages))
paper_text = "\n".join([page.page_content for page in pages[:pages_to_scan]])

# 3. Modular LLM Setup (API Agnostic configuration)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)
structured_llm = llm.with_structured_output(BETYdbExperimentIR)

# 4. Extractor Agent Execution
result = structured_llm.invoke(paper_text)
print(result.model_dump_json(indent=2))
