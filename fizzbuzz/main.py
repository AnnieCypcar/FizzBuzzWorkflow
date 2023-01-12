import functions_framework
from flask import jsonify


@functions_framework.http
def fizzbuzz(request):
    request_json = request.get_json()
    num = request_json['input']
    output = []
    num_int = int(num)
    if num_int > 1 and num_int < 1000:
        output = [str(i+1) for i in range(num_int)]
    return jsonify(output)
