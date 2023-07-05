from sklearn.model_selection import train_test_split
import pandas as pd
import sys
df = pd.read_csv('data.csv')

df.drop(['id','Unnamed: 32'],axis=1, inplace=True)
# print(df)
X,y = df.drop('diagnosis',axis=1), df['diagnosis'].values

x_train,x_test,y_train,y_test = train_test_split(X,y)

SQL_DB = pd.concat([pd.DataFrame(x_train),pd.Series(y_train)],axis=1, join='inner')
TEST_DB = pd.concat([pd.DataFrame(x_test),pd.Series(y_test)],axis=1, join='inner')

SQL_DB.to_csv('train.csv',index=False)
TEST_DB.to_csv('test.csv',index=False)

# import IPython; IPython.embed();sys.exit(1)