# %%
import requests
import json

# %%
url = "http://127.0.0.1:11434/api/generate"

payload = {
   "model": "llama3.1",
  "prompt": "Hello! Who are you?",
  "stream": False
}

try:
   response = requests.post(url, json=payload)
   response.raise_for_status()
   result = response.json()
   print(result["response"])
except requests.exceptions.RequestException as e:
   print(f"Error: {e}")

# %%
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

# %%
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(model="llama3.1", request_timeout=60.0)

# %%
from llama_index.core import SimpleDirectoryReader
documents = SimpleDirectoryReader("./data").load_data()

# %%
from llama_index.core import VectorStoreIndex
index = VectorStoreIndex.from_documents(documents)

# %%
query_engine = index.as_query_engine()

# %%
response = query_engine.query("What is LuminaBloom Foundation?")
print(response)


