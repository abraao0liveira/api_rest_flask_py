from flask import jsonify

def response_model(status_code, message=None, data=None, error=None):
  response = {
    'status_code': status_code,
    'message': message,
    'data': data,
    'error': error
  }
  
  response = {key: value for key, value in response.items() if value is not None} # remove os valores nulos

  return jsonify(response), status_code
