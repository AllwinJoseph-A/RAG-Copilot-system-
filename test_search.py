import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def test_local_search():
    # 1. Re-initialize the exact same local embedding model
    print("Loading local embedding model...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # 2. Load the local FAISS index from the folder
    print("Loading local FAISS vector index...")
    # allow_dangerous_deserialization is required to load local pickle files safely
    vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    
    # 3. Define a natural language question (no SQL keywords!)
    query = "Who knows how to build neural networks and write SQL queries?"
    print(f"\nUser Query: '{query}'")
    print("Searching vector space for top matches...")
    
    # 4. Perform the similarity search
    # k=1 means we want the single closest match
    results = vector_store.similarity_search(query, k=1)
    
    # 5. Print the winner
    if results:
        print("\n--- Top Retrieved Context ---")
        print(results[0].page_content)
        print("------------------------------")
    else:
        print("No matching context found.")

if __name__ == "__main__":
    test_local_search()