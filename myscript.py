# my_lambdata/my_mod.py
from sklearn.model_selection import train_test_split
import pandas

def splitter(df):

    test, train = train_test_split(df, test_size = 0.7, random_state=42)

    val, train = train_test_split(train, test_size = 0.7, random_state=24)

    return (train.shape, val.shape, test.shape)

if __name__ == "__main__":

    #test, train = train_test_split(df, test_size = 0.7, random_state=42)

    #val, train = train_test_split(train, test_size = 0.7, random_state=24)

    print('hello')
    #print (train.shape, val.shape, test.shape)