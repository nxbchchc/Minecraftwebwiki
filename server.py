from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")

    return jsonify({"reply": f"You said: {message}. This is Render AI server response."})

app.run(host="0.0.0.0", port=10000)
