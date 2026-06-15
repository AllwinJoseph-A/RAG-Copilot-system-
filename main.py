import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from query_rag import run_rag_query
from rag_engine import build_unified_vector_index

app = FastAPI()

class ChatRequest(BaseModel):
    question: str

@app.post("/api/upload")
async def upload_document(file: UploadFile = File(...)):
    docs_folder = "documents"
    if not os.path.exists(docs_folder):
        os.makedirs(docs_folder)
    
    # Save the file (this overwrites if a file exists)
    file_path = os.path.join(docs_folder, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    # Rebuild the brain
    build_unified_vector_index()
    return {"message": "File processed successfully"}

@app.post("/api/ask")
def ask_copilot(request: ChatRequest):
    answer = run_rag_query(request.question)
    return {"answer": answer}