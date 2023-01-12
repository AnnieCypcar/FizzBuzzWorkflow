import functions_framework
from flask import jsonify


@functions_framework.http
def fizz(request):
    request_json = request.get_json()
    input = request_json['input']
    for i in range(len(input)):
        if type(input[i]) == int:
            if input[i] % 3 == 0:
                input[i] = "Fizz"
    return jsonify(input)