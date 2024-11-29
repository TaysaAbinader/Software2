from flask import Flask, request, Response
import json

from Module12Class.Module_12 import json_response

app = Flask(__name__)
@app.route('/sum')
def calculate_sum():
    try:
        args = request.args
        number1 = float(args.get("number1"))
        number2 = float(args.get("number2"))
        total_sum = number1 + number2
        #return str(total_sum)
        response = {
            "Greeting": "Hello hello!",
            "First number": number1,
            "Second number": number2,
            "Result": total_sum}
        return json.dumps(response)
    except ValueError:
        response = {
            "message": "Invalid input is added"
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response = json_response, status=400, mimetype = 'application/json')
        return http_response

@app.route('/product')
def calculate_product():
    args = request.args
    number1 = float(args.get("number1"))
    number2 = float(args.get("number2"))
    product = number1 + number2
    return str(product)

@app.route('/hello')
def hello_world():
    return "Hello, World!"

@app.route('/echo/<text>')
def echo(text):
    response = {
        "echo": text + "" + text,
        "question":"do you really mean" + text +"?"
    }
    return json.dumps(response)


@app.error_handler(404)
def page_not_found(error_code):
    response = {
        "message":"Invalid Endpoint",
        "status":404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype='application/json')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=8000)