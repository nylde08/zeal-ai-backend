from flask import Flask, request, jsonify
import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

app = Flask(__name__)

# Load API key from Railway
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")
client = MistralClient(api_key=MISTRAL_API_KEY)

@app.route("/", methods=["GET"])
def home():
    return "ZEAL.AI backend is alive"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    messages = [
        ChatMessage(role="system", content="You are ZEAL.AI, a Bible-based assistant."),
        ChatMessage(role="user", content=user_message)
    ]

    response = client.chat(
        model="mistral-small",
        messages=messages
    )

    reply = response.choices[0].message.content

    return jsonify({
        "reply": reply,
        "assistant": "ZEAL.AI"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
