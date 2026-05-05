# RAG E-Commerce Product Search
## How It Works
 
1. Each product's name, description, and attributes are embedded into a 384-dimensional vector using `all-MiniLM-L6-v2` and stored in ChromaDB
2. The user types a natural language query — the same model converts it into a vector
3. ChromaDB finds the most semantically similar products using cosine similarity
4. Results are returned with name, description, and price
---
 
## Tech Stack
 
- Python 3.11
- ChromaDB
- sentence-transformers (`all-MiniLM-L6-v2`)
- PyTorch (CPU)
---
 
## Setup
 
> ⚠️ Use Python 3.11. PyTorch does not support Python 3.13 on Windows.
 
```
py -3.11 -m venv venv
venv\Scripts\activate
pip install chromadb sentence-transformers torch --index-url https://download.pytorch.org/whl/cpu
python main.py   # ingest products
python search.py # run search
```
 
> **Windows:** If you hit a DLL error, install [Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe) and restart.
 
---
 
## Example Queries
 
**"anything that keeps me warm"**
```
Name: Insulated Puffer Vest | Price: $119.00
Name: Fleece Midlayer Pullover | Price: $99.00
Name: Merino Wool Beanie | Price: $34.99
```
 
**"waterproof jacket for hiking"**
```
Name: Trailmaster Waterproof Shell Jacket | Price: $149.99
Name: Rain Pants Lightweight | Price: $79.00
```
 
---
 
## Project Structure
 
```
rag-ecommerce-search/
├── data/products.json   ← product catalog
├── main.py              ← ingestion pipeline
├── search.py            ← query pipeline
└── README.md
