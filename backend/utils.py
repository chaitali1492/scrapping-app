import openai
import numpy as np
from config import OPENAI_API_KEY
from mognodb import fetchEmbedding

openai.api_key = OPENAI_API_KEY

def getEmbeddings(str) :

    # Call the embeddings endpoint
    response = openai.embeddings.create(
        model="text-embedding-3-small", 
        input=str
    )

    # Extract the embedding vector
    embedding_vector = response.data[0].embedding
    return embedding_vector

def cosine_similarity(a: list, b: list) -> float:
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def find_top_k_similar(embedding, k=3):
    all_docs = list(fetchEmbedding())
    for doc in all_docs:
        doc["similarity"] = cosine_similarity(embedding, doc["embedding"])
    top_docs = sorted(all_docs, key=lambda x: x["similarity"], reverse=True)[:k]
    return top_docs


def get_answer_from_context(question, context):
    prompt = f"Use the context below to answer the question:\n\nContext:\n{context}\n\nQuestion: {question}"
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()
