from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

messages = []

@app.route("/")
def home():
    return render_template("index.html", messages=messages)

@app.route("/add-message", methods=["POST"])
def add_message():
    data = request.get_json()

    message = data.get("message")

    if message:
        messages.append(message)

    return jsonify({
        "success": True,
        "messages": messages
    })

if __name__ == "__main__":
    app.run(debug=True)
