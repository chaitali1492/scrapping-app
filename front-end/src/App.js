import { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setResponse("");

    try {
      const res = await fetch("http://localhost:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });

      if (!res.ok) throw new Error("Network response was not ok");

      const data = await res.json();
      setResponse(data.answer || "No answer returned.");
    } catch (err) {
      setResponse("Error: " + err.message);
    }
    setLoading(false);
  }

  return (
    <div style={{ maxWidth: 600, margin: "2rem auto", fontFamily: "Arial" }}>
      <h2>Ask your question:</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Type your question here"
          style={{ width: "100%", padding: "0.5rem", fontSize: "1rem" }}
          required
        />
        <button type="submit" disabled={loading} style={{ marginTop: "1rem" }}>
          {loading ? "Loading..." : "Submit"}
        </button>
      </form>

      {response && (
        <div
          style={{
            marginTop: "2rem",
            padding: "1rem",
            border: "1px solid #ddd",
            borderRadius: 4,
            backgroundColor: "#f9f9f9",
          }}
        >
          <strong>Response:</strong>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}

export default App;
