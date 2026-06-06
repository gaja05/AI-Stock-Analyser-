import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    const thinkingMessage = {
  sender: "bot",
  text: "Thinking..."
};

setMessages((prev) => [
  ...prev,
  userMessage,
  thinkingMessage
]);

    try {
      const response = await axios.get("http://127.0.0.1:8000/analyse", {
        params: { stock: input },
      });

      const botMessage = {
  sender: "bot",
  text: response.data.analysis,
};

setMessages((prev) => {
  const updated = [...prev];

  updated[updated.length - 1] = botMessage;

  return updated;
});
      setInput("");
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "Error calling backend API" },
      ]);
    }
  };

  return (
    <div className="chat-container">
      <h2>L1 Stock Reader</h2>

      <div className="chat-box">
        {messages.map((msg, index) => (
          <div key={index} className={msg.sender === "user" ? "user" : "bot"}>
            {msg.text}
          </div>
        ))}
      </div>

      <div className="input-box">
        <input
          type="text"
          placeholder="Enter stock name"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => {
    if (e.key === "Enter") {
      sendMessage();
    }
  }}
        />

        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;