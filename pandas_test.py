__author__ = 'changyunglin'
import pandas

fileName = '/Users/changyunglin/Dropbox/STA250/test.csv'
df = pandas.read_csv(fileName)
a = df.mean(axis={columns (14)}, skipna=True, level=None)
print(a)


