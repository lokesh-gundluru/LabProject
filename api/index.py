# === PROGRAM STORAGE ===
programs = {
    "1": "print('Program 1 working')",
    "2": "print('Program 2 working')"
}

# === HANDLER ===
def handler(request):
    try:
        # Get path safely
        path = request.get("path", "")
        num = path.split("/")[-1]

        code = programs.get(num, "Program not found")

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/plain"},
            "body": code
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }

# === REQUIRED EXPORT ===
app = handler