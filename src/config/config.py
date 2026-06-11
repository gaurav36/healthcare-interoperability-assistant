import os
from pathlib import Path
import json

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = ROOT_DIR / ".env"
CONFIG_JSON_PATH = ROOT_DIR / "config.json"

load_dotenv(ENV_PATH)

# Load configuration from config.json if available
config_data = {}
if CONFIG_JSON_PATH.exists():
    try:
        with open(CONFIG_JSON_PATH, "r", encoding="utf-8") as f:
            config_data = json.load(f)
    except Exception as e:
        print(f"Warning: Failed to load config.json: {e}")


def get_config_val(key: str, default: str) -> str:
    val = config_data.get(key)
    if val is not None:
        return str(val).strip()
    return os.getenv(key, default).strip()


def get_openai_api_key() -> str:
    load_dotenv(ENV_PATH)
    return os.getenv("OPENAI_API_KEY", "").strip()


def has_openai_api_key() -> bool:
    key = get_openai_api_key()
    return bool(key and key != "sk-your-key-here")


def get_groq_api_key() -> str:
    load_dotenv(ENV_PATH)
    return os.getenv("GROQ_API_KEY", "").strip()


def has_groq_api_key() -> bool:
    key = get_groq_api_key()
    return bool(key and key != "gsk-your-key-here")


OPENAI_API_KEY: str = get_openai_api_key()
GROQ_API_KEY: str = get_groq_api_key()

# Configuration switches
LLM_PROVIDER: str = get_config_val("LLM_PROVIDER", "openai").lower()
EMBEDDING_PROVIDER: str = get_config_val("EMBEDDING_PROVIDER", "openai").lower()

# Model Names (Defaults)
LLM_MODEL: str = get_config_val("LLM_MODEL", "gpt-4o-mini" if LLM_PROVIDER == "openai" else "llama-3.3-70b-versatile")
EMBEDDING_MODEL: str = get_config_val("EMBEDDING_MODEL", "text-embedding-3-small" if EMBEDDING_PROVIDER == "openai" else "all-MiniLM-L6-v2")

CHUNK_SIZE: int = 500
CHUNK_OVERLAP: int = 50
RETRIEVER_K: int = 4


def is_llm_configured() -> bool:
    if LLM_PROVIDER == "openai":
        return has_openai_api_key()
    elif LLM_PROVIDER == "groq":
        return has_groq_api_key()
    return False


def is_embeddings_configured() -> bool:
    if EMBEDDING_PROVIDER == "openai":
        return has_openai_api_key()
    elif EMBEDDING_PROVIDER == "huggingface":
        return True
    return False


def is_system_configured() -> bool:
    return is_llm_configured() and is_embeddings_configured()