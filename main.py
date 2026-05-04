import chromadb
import json
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

client = chromadb.Client()

embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2") #Not necessary, but it will make the search more accurate. You can also use the default embedding function, which is based on OpenAI's text-embedding-3-small.
collection = client.get_or_create_collection(
    name="products",
    embedding_function=embedding_function
)

with open("data/products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

for product in products:
    collection.add(
        ids=[product["productCode"]],
        documents=[product["description"]+"."+product["name"]+"."+product["category"]],
        metadatas=[{
    "price": product["price"],
    "category": product["category"],
    "stock": product["stock"]["stockLevel"],
    "gender": product["attributes"].get("gender", "Unisex")
} ]
    )

print(collection.peek(5))
print(collection.count())