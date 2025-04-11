import os
from app.vector_store import load_vector_store
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

db = load_vector_store("app/pdf_vector_db")

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY")),
    chain_type="stuff",
    retriever=db.as_retriever()
)

while True:
    question = input("Tanyakan tentang topik Cyber Security: ")
    if question.lower() in ["exit", "quit"]:
        break
    answer = qa.run(question)
    print(f"Answer: {answer}")
