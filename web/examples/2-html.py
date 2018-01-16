from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('2-html.html')

@app.route('/forms', methods=['POST'])
def forms():
  return 'You said: ' + request.form['text']

if __name__ == '__main__':
  app.run(debug=True, port=8080)