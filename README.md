#  FastAPI Vector Search with MongoDB & OpenAI

This project is a simple question-answering system using **FastAPI**, **MongoDB**, and **OpenAI Embeddings**.

It works like this:
1. Text is broken into chunks and stored in MongoDB with their **OpenAI embeddings**.
2. When you ask a question, its embedding is calculated.
3. The app finds the **top 3 similar chunks** from MongoDB.
4. These chunks are sent to **OpenAI GPT model** to generate the final answer.

---

## 🔧 Technologies Used

- **FastAPI** – For creating the backend API
- **MongoDB** – To store documents and their vector embeddings
- **OpenAI API** – To generate embeddings and final answers
- **Pydantic** – For request validation
- **Python** – Core language

---


##  How to Run the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Your Environment Variables

In `config.py` file set:

```bash
OPENAI_API_KEY=your_openai_key
```

### 3. Start the web application

```bash
npm install
npm start
```

### 4. Start the FastAPI Server

```bash
uvicorn backend.main:app --reload
```

Application will run on: [http://127.0.0.1:8000/](http://127.0.0.1:8000)

---

##  API Endpoints

### 1. `/ask`
- **Method:** POST
- **Description:** Ask a question. Returns answer based on closest content.
- **Request:**
```json
{
  "question": "What is mission?"
}
```


