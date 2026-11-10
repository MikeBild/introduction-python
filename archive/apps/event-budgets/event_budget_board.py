#!/usr/bin/env python3

import pandas
from glob import glob
from event_budget import load_event_buget

def event_budget_board():
    all_event_files = glob('python-in-a-nutshell-data/*.xlsx')
    return pandas.concat(load_event_buget(f) for f in all_event_files)

def group_by_place_and_category(func):
  def wrapper():
    return func().groupby(['Place', 'Category']).agg({'Total': sum})
  return wrapper

def to_bar_plot(func):
  def wrapper():
    return func()['Total'].unstack('Category').plot(kind='bar', title='Totals by Place & Category', stacked=True, figsize=(17,10))
  return wrapper

if __name__ == '__main__':
  plot = to_bar_plot(group_by_place_and_category(event_budget_board))()
  plot.get_figure().savefig('board.png')
