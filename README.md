Here is a comprehensive, production-ready `README.md` file tailored specifically for your project structure, tech stack, and ingestion pipeline.

You can create a file named `README.md` in your `workforce-copilot/backend` directory and paste this content right inside.

---

# Enterprise Workforce Copilot & Multi-Source RAG System

An intelligent, context-aware Retrieval-Augmented Generation (RAG) pipeline designed to bridge the gap between structured organizational data and unstructured corporate documents. This application unifies SQLite relational employee records with PDF-based documents (such as candidate resumes) into a localized, ultra-secure vector ecosystem, completely decoupled from external third-party cloud API dependencies.

---

## 🚀 Key Features

* **Structured Data Extraction:** Parses employee profiles, salaries, roles, and expertise from a local SQLite engine.
* **Dynamic Unstructured Parsing:** Automatically scans local directories to read, split, and chunk multi-page PDF documents.
* **Unified Vector Indexing:** Blends multi-source operational streams into a singular local **FAISS** vector store using highly accurate open-source embeddings.
* **100% Local Intelligence:** Leverages **Ollama** (`llama3`) locally to synthesize document context and format professional, conversational responses.
* **Modular Multi-Tier Architecture:** Built with a blazing-fast **FastAPI** backend service coupled with an intuitive **Streamlit** interactive dashboard.

---

## 🛠️ Tech Stack

* **Frontend Dashboard:** Streamlit
* **API Service Layer:** FastAPI (Uvicorn server)
* **Orchestration Framework:** LangChain / LangChain-Ollama / LangChain-Community
* **Vector Store:** Facebook AI Similarity Search (FAISS)
* **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2` (Local HuggingFace model)
* **Local Inference Engine:** Ollama (`llama3`)
* **Relational Store:** SQLite3

---

## 📂 Project Structure

```text
workforce-copilot/text
└── backend/
    ├── documents/               # Folder where source PDFs/Resumes are dropped
    ├── faiss_index/             # Saved local vector store binary data (Generated)
    ├── __pycache__/             # Compiled Python bytecode files
    ├── venv/                    # Local Python virtual environment
    ├── .env                     # Local infrastructure configurations/keys
    ├── .gitignore               # Strict ignore layouts to prevent tracking secrets
    ├── chat_ui.py               # Streamlit interactive UI application
    ├── init_db.py               # Database migration script for mock records
    ├── main.py                  # Core FastAPI application endpoints
    ├── query_rag.py             # Vector lookup engine & local LLM synthesis pipeline
    ├── rag_engine.py            # Document parsing and vector compilation framework
    ├── requirements.txt         # Consolidated Python dependencies index
    └── workforce.db             # Core relational production SQLite database

```

---

## 🔧 Installation & Setup

### Prerequisites

* Python 3.10 or higher installed on your host system.
* Ollama installed and configured locally.

### 1. Set Up Environment Variables

Create a file named `.env` in the root backend directory to contain localized development configs:

```env
PORT=8000
HOST=127.0.0.1

```

### 2. Configure Local AI Engine

Ensure Ollama is actively running on your local daemon and pull the target Large Language Model model:

```powershell
ollama pull llama3
ollama run llama3

```

### 3. Initialize Python Environment & Dependencies

Open your choice of terminal, navigate to the backend directory, activate your isolation virtual environment, and install the required modules:

```powershell
# Navigate to project root
cd "D:\New folder (2)\workforce-copilot\backend"

# Activate the virtual environment
.\venv\Scripts\activate

# Install required LangChain and deployment packages
pip install -r requirements.txt

```

### 4. Seed the Relational Database

Run your initialization script to spin up the local SQLite instance and inject dummy structural corporate data:

```powershell
python init_db.py

```

---

## 🏃 Execution Pipeline

To boot up the complete framework, run the backend API service alongside the user interface client across distinct terminal lines.

### Step A: Run the FastAPI Application

```powershell
uvicorn main:app --reload

```

> Ensure the console outputs `INFO: Application startup complete` on port `8000`.

### Step B: Run the Streamlit Dashboard UI

```powershell
streamlit run chat_ui.py

```

> This will automatically forward and spin up a browser container pointing to `http://localhost:8501`.

---

## 📖 Processing Lifecycle & Usage

1. **Ingestion Execution:** Log into your Streamlit interface, access the document interface section, and drop a target file (e.g., a technical resume PDF) into the processing pane.
2. **Knowledge Synthesis:** Press **"Process & Learn Document"**. The system executes `rag_engine.py`, reads the data, and outputs an confirmation reading `"Unified multi-source vector database successfully built!"` onto your FastAPI tracking log.
3. **Contextual Inquiries:** Enter human-readable analytical inquiries directly into the conversational layout box (e.g., `"List the skills"` or `"What projects are documented?"`). The RAG pipeline matches the similarity indices, packages a structured payload prompt context, and returns stylized, bulleted layouts back to the browser panel instantly.
