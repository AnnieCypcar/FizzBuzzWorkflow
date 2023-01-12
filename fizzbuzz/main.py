import functions_framework
from flask import jsonify


@functions_framework.http
def fizz(request):
    request_json = request.get_json()
    num = request_json['n']
    output = [str(i+1) for i in range(num)]
    return jsonify(output)