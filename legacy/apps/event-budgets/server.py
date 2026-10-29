from flask import Flask, Response
from io import BytesIO
from event_budget_board import group_by_place_and_category, event_budget_board, to_bar_plot

app = Flask(__name__)

@app.route('/board')
def board_as_json():
  return Response(group_by_place_and_category(event_budget_board)().reset_index().to_json(), mimetype='application/json')

@app.route('/plot')
def board_as_plot():
  img = BytesIO()
  plot = to_bar_plot(group_by_place_and_category(event_budget_board))()
  plot.get_figure().savefig(img, format='png')
  img.seek(0)
  return Response(img, mimetype='image/png')

if __name__ == '__main__':
  app.run(debug=True, port=8080)