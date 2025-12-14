from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def home():
    return "ZEAL.AI is alive."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are ZEAL.AI, a Bible-based assistant that gives wise, gentle, scripture-aligned responses."
                },
                {"role": "user", "content": message}
            ]
        )

        reply = response.choices[0].message.content

        return jsonify({
            "reply": reply,
            "name": "ZEAL.AI"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
