from fastapi import FastAPI
from pydantic import BaseModel
from app.utils import extract_text_from_pdfs
from app.gemini import get_fine_prints, chat_with_context
import json

app = FastAPI()

doc_text = None

@app.get("/")
def home():
    return {"message": "RAG system is running."}

@app.get("/fine-prints")
def fine_prints():
    global doc_text
    doc_text = extract_text_from_pdfs("data")
    fine_result = get_fine_prints(doc_text)

    with open("fine_prints.txt", "w", encoding="utf-8") as f:
        f.write(fine_result)

    return {"fine_prints": fine_result}

@app.post("/chat")
def chat_with_rag():
    try:
        with open("fine_prints.txt", "r", encoding="utf-8") as f:
            fine_prints = f.read()

        with open("sample_questions.txt", "r", encoding="utf-8") as f:
            questions = [line.strip() for line in f if line.strip()]

        results = []
        for question in questions:
            answer = chat_with_context(fine_prints, question)
            results.append({"question": question, "answer": answer})

        with open("chat_response.txt", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)

        return {"chat": results}

    except Exception as e:
        return {"error": str(e)}
