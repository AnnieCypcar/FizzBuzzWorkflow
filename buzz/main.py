import functions_framework
from flask import jsonify


@functions_framework.http
def buzz(request):
    request_json = request.get_json()
    input = request_json['input']
    for i in range(len(input)):
        if input[i] % 5 == 0:
            input = 'Buzz'
    return jsonify(input)
