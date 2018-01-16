import pandas as pd

# Series
series = pd.Series([1, 2.1, 3], index=['a', 'b', 'c'], dtype=int)
print('Series:', series)

# DataFrame
data = {
  'Country': ['Germany', 'India', 'Swiss'],
  'Capital': ['Berlin', 'New Delhi', 'Bern'],
  'Population': [82457000, 1339180000, 8401000, ]
}

df = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])
print('DataFrame:', df)