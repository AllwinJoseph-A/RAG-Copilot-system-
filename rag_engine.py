import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def build_unified_vector_index():
    # Ensure consistency: Save to a fixed folder named 'faiss_index'
    save_path = "faiss_index"
    docs_folder = "documents"
    
    # Load and split documents
    all_docs = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    
    for file in os.listdir(docs_folder):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(docs_folder, file))
            all_docs.extend(splitter.split_documents(loader.load()))

    # Build and Save
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(all_docs, embeddings)
    vector_store.save_local(save_path)
    print("Unified vector database successfully built!")