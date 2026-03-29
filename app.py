from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI
import os


load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])
    print("Received messages:", messages)
    if not messages:
        return jsonify({"reply": "Please enter a message."}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception:
        return jsonify({"reply": "Sorry, the AI service is currently unavailable. Please try again later."}), 500


if __name__ == "__main__":
    app.run(debug=True)