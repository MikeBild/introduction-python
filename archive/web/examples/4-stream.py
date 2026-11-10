from flask import Flask, stream_with_context, request, Response

app = Flask(__name__)

@app.route('/stream')
def streamed_response():
  @stream_with_context
  def generate():
    yield 'Hello;'
    yield request.args['name']
  return Response(generate(), mimetype='text/csv')

if __name__ == '__main__':
  app.run(debug=True, port=8080)