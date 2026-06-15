import streamlit as st
import requests

st.title("Workforce Copilot")
uploaded_file = st.sidebar.file_uploader("Upload PDF", type="pdf")

if uploaded_file and st.sidebar.button("Process & Learn"):
    files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
    response = requests.post("http://127.0.0.1:8000/api/upload", files=files)
    if response.status_code == 200:
        st.success("Brain Updated!")

prompt = st.chat_input("Ask a question...")
if prompt:
    response = requests.post("http://127.0.0.1:8000/api/ask", json={"question": prompt})
    st.write(response.json().get("answer"))