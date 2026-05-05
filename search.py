import chromadb
import json
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

client = chromadb.PersistentClient("./chroma_db")
embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
collection = client.get_collection(
    name="products",
    embedding_function=embedding_function
)

query = input("What product are you looking for? ")
results = collection.query(
    query_texts=[query],
    n_results=5
)

for i in range(len(results["ids"][0])):
    print(f"Name: {results['metadatas'][0][i]['name']}")
    print(f"Description: {results['metadatas'][0][i]['description']}")
    print(f"Price: {results['metadatas'][0][i]['price']}")
