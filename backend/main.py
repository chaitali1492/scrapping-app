from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from utils import  find_top_k_similar, get_answer_from_context, getEmbeddings

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: Query):
    try:
        question = query.question
        embedding = getEmbeddings(question)
        top_docs = find_top_k_similar(embedding, k=3)

        if not top_docs:
            return {"answer": "No relevant information found."}

        combined_context = "\n\n".join(doc["content"] for doc in top_docs)
        answer = get_answer_from_context(question, combined_context)
        return {
            "question": question,
            "answer": answer
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
