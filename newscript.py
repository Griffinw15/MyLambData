from sklearn.model_selection import train_test_split
import pandas

from MyLambData.myscript import splitter

df = pandas.DataFrame({'Number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]})


print(df.head())
print(splitter(df))