from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/json', methods=['GET', 'POST'])
def get_username():
  print('Request:', request.json)

  res = {
    'username': 'John Doe',
  }

  if request.json:
    res.update(request.json)
  else: res

  return jsonify(res)

if __name__ == '__main__':
  app.run(debug=True, port=8080)