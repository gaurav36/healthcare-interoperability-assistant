import os
from langchain_openai import ChatOpenAI
from pathlib import Path
from dotenv import load_dotenv
root_dir = Path(__file__).resolve().parent.parent.parent
load_dotenv(root_dir / ".env")


class LLMService:
    def __init__(self):
        self.llm, self.embed_model = self._init_models()

    def _init_models(self):
        llm_model = os.getenv("LLM_MODEL", "openai/gpt-oss-120b")

        openai_api_key = os.getenv("OPENAI_API_KEY")
        groq_api_key = os.getenv("GROQ_API_KEY")

        if not openai_api_key and not groq_api_key:
            raise ValueError("No API keys found. Please set OPENAI_API_KEY or GROQ_API_KEY in .env")

        if groq_api_key:
            print("Using Groq API")
            llm = ChatOpenAI(
                model=llm_model,
                base_url="https://api.groq.com/openai/v1",
                api_key=groq_api_key,
                temperature=0.2,
            )
        else:
            print("Using OpenAI API")
            llm = ChatOpenAI(
                model=llm_model,
                api_key=openai_api_key,
                temperature=0.2,
            )

        embedding_model_name = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

        # embeddings
        print(f"Loading embedding model: {embedding_model_name}...")
        try:
            from langchain_huggingface import HuggingFaceEmbeddings
            embed = HuggingFaceEmbeddings(
                model_name=embedding_model_name
            )
        except ImportError:
            print("Warning: langchain-huggingface not installed. Using default OpenAI embeddings.")
            from langchain_openai import OpenAIEmbeddings
            embed = OpenAIEmbeddings(
                model="text-embedding-3-small",
                    openai_api_key=openai_api_key
            )

        return llm, embed