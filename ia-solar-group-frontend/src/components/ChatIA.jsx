// src/components/ChatIA.jsx
import React, { useState } from "react";

const ChatIA = () => {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setError(null);

    try {
      const response = await fetch("http://localhost:8000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ question }),
      });

      if (!response.ok) {
        throw new Error(`Erro: ${response.status}`);
      }

      const data = await response.json();
      setAnswer(data.answer);
    } catch (err) {
      setError("Erro ao conectar com a IA.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: "2rem auto", padding: "1rem" }}>
      <h1>🤖 IA Solar Group</h1>
      <p>Pergunte abaixo:</p>

      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Digite sua pergunta..."
        style={{ width: "100%", padding: "0.5rem" }}
      />

      <button
        onClick={handleAsk}
        style={{ marginTop: "1rem", padding: "0.5rem 1rem" }}
        disabled={loading}
      >
        {loading ? "Consultando..." : "Perguntar"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {answer && (
        <div style={{ marginTop: "1rem", background: "#f5f5f5", padding: "1rem" }}>
          <strong>Resposta:</strong>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
};

export default ChatIA;
