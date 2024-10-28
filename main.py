from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi import Request

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def bertoxcalculator():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple Calculator</title>
        <style>
            body { font-family: Arial, sans-serif; }
            form { margin: 20px; }
            input, select { padding: 10px; margin: 5px; }
            button { padding: 10px 15px; }
            .result { margin-top: 20px; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>Simple Calculator</h1>
        <form action="/calculate" method="get">
            <input type="number" name="num1" placeholder="Number 1" required>
            <select name="operation" required>
                <option value="+">+</option>
                <option value="-">-</option>
                <option value="*">*</option>
                <option value="/">/</option>
            </select>
            <input type="number" name="num2" placeholder="Number 2" required>
            <button type="submit">Calculate</button>
        </form>
    </body>
    </html>
    """

@app.get("/calculate", response_class=HTMLResponse)
def calculate(operation: str, num1: float, num2: float):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        result = "Invalid operation"

    return f"""
    <html>
    <body>
        <h1>Calculation Result</h1>
        <p>The result of {num1} {operation} {num2} is: {result}</p>
        <a href="/">Go Back</a>
    </body>
    </html>
    """
