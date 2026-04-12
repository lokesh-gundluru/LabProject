from flask import Flask, request, Response

app = Flask(__name__)

# === PROGRAM STORAGE ===
programs = {
    "1": "print('Program 1 working')",
    "2": "print('Program 2 working')"
}

# === ROUTE ===
@app.route('/programs/<num>')
def get_program(num):
    code = programs.get(num, "Program not found")
    return Response(code, mimetype='text/plain')