import functions_framework
from flask import jsonify


@functions_framework.http
def buzz(request):
    request_json = request.get_json()
    input = request_json['input']
    for i in range(len(input)):
        if type(input[i]) == int:
            if input[i] % 5 == 0:
                input[i] = 'Buzz'
            else:
                input[i] = str(input[i])
    return jsonify({'answer': input})
