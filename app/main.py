from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from app.vector_store import load_vector_store
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.mount("/", StaticFiles(directory="static", html=True), name="static")

db = load_vector_store("app/pdf_vector_db")

print("Loaded Vector DB:", db)
print("Retriever docs example:", db.similarity_search("test"))

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY")),
    chain_type="stuff",
    retriever=db.as_retriever()
)

class Question(BaseModel):
    question: str

@app.post("/ask-pdf")
def ask_pdf(q: Question):
    answer = qa.run(q.question)
    return {"answer": answer}
