from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/prime_number')
def prime_number():
    try:
        args = request.args
        number = int(args.get("number"))
        if number <= 1:
            return json.dumps({"Number": number, "isPrime": False})

        is_prime = True
        for i in range(2, int(number)):
            if number % i == 0:
                is_prime = False
                break

        response = {"Number": number, "isPrime": is_prime}
        return json.dumps(response)

    except ValueError:
        response = {"message": "Invalid input. Please provide an integer."}
        return json.dumps(response), 400

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
