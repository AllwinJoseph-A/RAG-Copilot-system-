import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
# Replace OllamaLLM with ChatOpenAI or ChatGroq if you aren't using local models
from langchain_ollama import OllamaLLM 
from langchain_core.prompts import ChatPromptTemplate

# 1. Define a strict prompt layout for the LLM
PROMPT_TEMPLATE = """
You are a helpful assistant. Use the following pieces of retrieved context to answer the user's question accurately. 
If the answer cannot be found in the context, say "I cannot find that information in the document."

Context:
{context}

---

Question: {question}

Answer with clean formatting, bullet points where appropriate, and keep it highly readable:
"""

def run_rag_query(query):
    index_path = "faiss_index"
    
    if not os.path.exists(index_path):
        return "The AI brain has not been built yet. Please upload a PDF first."

    # 2. Load the vector store from disk
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
    
    # 3. Retrieve the top relevant chunks (we increase k slightly to give the LLM more context)
    results = vector_store.similarity_search(query, k=3)
    
    if not results:
        return "No relevant information found in the document."
    
    # Combine the text contents from all matching chunks
    context_text = "\n\n---\n\n".join([doc.page_content for doc in results])
    
    # 4. Initialize your LLM (Make sure Ollama is running in the background!)
    # If using OpenAI: llm = ChatOpenAI(model="gpt-4o", api_key="your_key")
    llm = OllamaLLM(model="llama3") 
    
    # 5. Format the prompt and run it through the model
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query)
    
    try:
        response = llm.invoke(prompt)
        return response
    except Exception as e:
        return f"Error communicating with the LLM: {str(e)}. Make sure your LLM server/Ollama is running!"