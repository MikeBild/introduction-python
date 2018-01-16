#!/usr/bin/env python3

import pandas

def load_event_buget(f):
  event_buget = pandas.read_excel(f, index_col='Description').transpose()
  id = event_buget['Date']['Content'].strftime('%d-%m-%y')
  event_buget.insert(0, 'Id', id)
  expenses = pandas.read_excel(f, sheet_name='Expenses')
  expenses.insert(0, 'Id', id)
  expenses = expenses.assign(Total = lambda x: x.Units * x.Estimate)
  event_buget = expenses.merge(event_buget, on='Id').dropna(axis=1)
  return event_buget

def group_by_category(func):
  def wrapper(f):
    expenses = func(f)
    return expenses.groupby(['Category']).agg({'Total': [sum, min, max]})
  return wrapper

def to_pie_plot(func):
  def wrapper(f):
    grouped = func(f)
    return grouped['Total']['sum'].plot(kind='pie', title='Totals by Category', autopct='%1.1f%%', figsize=(17,10))
  return wrapper

@to_pie_plot
@group_by_category
def __as_bar_plot(f):
  return load_event_buget(f)

if __name__ == '__main__':
  plot = __as_bar_plot('python-in-a-nutshell-data/Q1-18-python-in-a-nutshell.xlsx')
  plot.get_figure().savefig('output.png')

# if __name__ == '__main__':
#   plot = to_pie_plot(group_by_category(load_event_buget))('python-in-a-nutshell-data/Q1-18-python-in-a-nutshell.xlsx')
#   plot.get_figure().savefig('output.png')
