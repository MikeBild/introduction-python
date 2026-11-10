from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!', 202

if __name__ == '__main__':
  app.run(debug=True, port=8080)