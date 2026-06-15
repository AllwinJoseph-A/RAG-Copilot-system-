from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def test_in_memory_extraction():
    # 1. Create the document text directly in memory (No hard drive needed!)
    print("Creating corporate policy document in memory...")
    policy_content = (
        "Corporate Policy Handbook\n\n"
        "Policy Rule SEC-2026: Working remote from international locations requires written corporate approval.\n"
        "All software developers must complete monthly network filtering and code vulnerability assessments.\n"
        "The corporate headquarters is officially moving to a new office suite in Chennai next quarter."
    )
    
    # 2. Wrap it in a LangChain Document object 
    # (This is exactly what TextLoader or PyPDFLoader does behind the scenes)
    doc = Document(page_content=policy_content, metadata={"source": "memory_test"})
    print(f"Successfully created document! Character length: {len(doc.page_content)}")

    # 3. Slice the text into chunks with an overlap buffer
    print("\n--- Slicing Text into Overlapping Chunks ---")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=150,     # Max characters per chunk
        chunk_overlap=30    # Overlapping characters between chunks
    )
    
    # Pass our memory document into the splitter
    chunks = text_splitter.split_documents([doc])
    print(f"Successfully generated {len(chunks)} text chunks.\n")
    
    for i, chunk in enumerate(chunks):
        print(f"--- Chunk {i+1} ---")
        print(chunk.page_content.strip())
        print("-" * 20)

if __name__ == "__main__":
    test_in_memory_extraction()