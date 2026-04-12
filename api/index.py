programs = {
    "1": "print('Program 1')",
    "2": "print('Program 2')"
}

def handler(request):
    path = request.path.split("/")[-1]
    code = programs.get(path, "Program not found")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": code
    }