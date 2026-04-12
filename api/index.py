from flask import Flask, Response
import os

app = Flask(__name__)

# === FOLDER PATH ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROG_DIR = os.path.join(BASE_DIR, "..", "progms")

# === HELPER FUNCTION ===
def load_program(num):
    filename_map = {
        "1": "one.txt",
        "2": "two.txt",
        "3": "three.txt",
        "4": "four.txt",
        "5": "five.txt",
        "6": "six.txt",
        "7": "seven.txt",
        "8": "eight.txt",
        "9": "nine.txt",
        "10": "ten.txt",
        "11": "eleven.txt",
        "12": "twelve.txt"
    }

    file = filename_map.get(num)
    if not file:
        return None

    file_path = os.path.join(PROG_DIR, file)

    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# === ROUTE ===
@app.route('/programs/<num>')
def get_program(num):
    code = load_program(num)

    if not code:
        return Response("Program not found", mimetype='text/plain')

    return Response(code, mimetype='text/plain')


# === OPTIONAL ROOT ===
@app.route('/')
def home():
    return "API working. Use /programs/<num>"