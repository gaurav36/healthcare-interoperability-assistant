# pyrefly: ignore [missingdd-import]
from dotenv import load_dotenv
import os
import uvicorn
import langchain
import langchain_core
import langchain_openai
import langchain_text_splitters
import faiss
import chromadb
import openai
import sentence_transformers
import pypdf
import python_multipart
import fastapi
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from src.llm.llm_service import LLMService


from pathlib import Path
root_dir = Path(__file__).resolve().parent.parent
load_dotenv(root_dir / ".env")

print(langchain.__version__)

def main():
    print("Hello from healthcare-interoperability-assistant!")
    llm_service = LLMService()
    llm = llm_service.llm
    
    response = llm.invoke("What is healthcare interoperability?")
    print (response.content)

if __name__ == "__main__":
    main()
