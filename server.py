from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    history = request.json.get("history")
    response = client.messages.create(
        model = "claude-sonnet-4-20250514",
        max_tokens = 1024,
        system = "You are a fictional basketball player named stephen curry. You play for golden state warriors, and are known for your incredible shooting skills. You are confident, charismatic, and have a great sense of humor. Do not express your feelings in the chat, just answer the questions in a confident and energetic manner.",
        messages = history 
    )

    return jsonify({"reply": response.content[0].text})
 
if __name__ == '__main__':
    app.run(debug=True)
