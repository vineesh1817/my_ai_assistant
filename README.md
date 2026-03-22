# 🏀 AI-Powered Chatbot — Chat with Steph Curry

A full stack AI web application built with Python, Flask, and the Anthropic Claude API. Chat with a fictional basketball player inspired by the style and energy of Stephen Curry of the Golden State Warriors.

🔗 **Live Demo:** https://my-ai-assistant-aidw.onrender.com

---

## 📸 Preview

> <img width="1470" height="880" alt="image" src="https://github.com/user-attachments/assets/41baa4a1-7554-4b7d-a67a-066454f52176" />


---

## 🚀 Features

- 💬 **Real-time AI chat** powered by Anthropic Claude API
- 🧠 **Conversation memory** — the bot remembers context across the entire chat
- 🎭 **Custom AI personality** via prompt engineering
- 🎨 **Clean chat UI** built with HTML, CSS, and JavaScript
- ☁️ **Deployed live** on Render cloud hosting

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| AI Model | Anthropic Claude (claude-sonnet-4-20250514) |
| Backend | Python, Flask, Flask-CORS |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Render |
| Version Control | Git, GitHub |

---

## 📁 Project Structure

```
my-ai-assistant/
├── .env                  ← API key (never commit this!)
├── .gitignore            ← ignores .env
├── requirements.txt      ← Python dependencies
├── server.py             ← Flask backend server
├── app.py                ← standalone Claude API script
└── templates/
    └── index.html        ← Chat UI frontend
```

---

## ⚙️ How It Works

```
User types a message
        ↓
JavaScript sends it to Flask /chat endpoint (POST)
        ↓
Flask passes full conversation history to Claude API
        ↓
Claude generates a reply in character
        ↓
Reply is sent back and displayed in the chat UI
```

---

## 🏃 Running Locally

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/my-ai-assistant.git
cd my-ai-assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
Create a `.env` file in the root folder:
```
ANTHROPIC_API_KEY=your-api-key-here
```
Get your API key at [console.anthropic.com](https://console.anthropic.com)

### 4. Run the server
```bash
python server.py
```

---

## 📦 Requirements

```
flask
flask-cors
anthropic
python-dotenv
gunicorn
```

---

## 💡 Key Concepts Used

- **REST API** — Flask `/chat` endpoint accepts POST requests
- **Prompt Engineering** — System prompt defines the AI's personality
- **Conversation History** — Full chat history sent to Claude on every message for context-aware replies
- **CORS** — Allows frontend and backend to communicate across ports
- **Environment Variables** — API key stored securely in `.env`

---

## 🌱 What I Learned

This was my first AI project as a sophomore CS student. Built during spring break, I learned:

- How APIs and API keys work
- Building a backend server with Flask
- Connecting a frontend to a backend
- Prompt engineering to shape AI behavior
- Git, GitHub, and cloud deployment with Render

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Sai Vineesh Pentyala**
- LinkedIn: [linkedin.com/in/sai-vineesh-pentyala](http://www.linkedin.com/in/sai-vineesh-pentyala)
- GitHub: [@vineesh1817](https://github.com/vineesh1817)
