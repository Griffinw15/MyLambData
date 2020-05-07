from sklearn.model_selection import train_test_split
import pandas

from MyLambData.myscript_class import Splitter

df = pandas.DataFrame({'Number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]})


#print(Splitter(df))

split = Splitter(df)
print(split.df.head())


#transformer = DataTransformer(df)
#print(transformer.df.head())
