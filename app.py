from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Game state variables
secret_number = random.randint(1, 100)
attempts = 0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    global secret_number, attempts
    data = request.get_json()
    user_guess = int(data.get("guess"))
    attempts += 1

    if user_guess < secret_number:
        return jsonify({"result": "low", "message": "Too low! 📈", "attempts": attempts})
    elif user_guess > secret_number:
        return jsonify({"result": "high", "message": "Too high! 📉", "attempts": attempts})
    else:
        # User guessed correctly
        winning_attempts = attempts
        # Reset game for next round
        secret_number = random.randint(1, 100)
        attempts = 0
        return jsonify({
            "result": "win", 
            "message": f"🎉 Bingo! You got it in {winning_attempts} attempts!", 
            "attempts": winning_attempts
        })

if __name__ == "__main__":
    app.run(debug=True)      