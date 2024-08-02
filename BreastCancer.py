import pandas
import pickle
from collections import Counter

Data = pandas.read_csv('DataSets/BreastCancer.csv')
Data = Data.drop(columns=['id'])

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
Data['diagnosis'] = le.fit_transform(Data['diagnosis'])

Y = Data.diagnosis
X = Data.drop(columns=['diagnosis'])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1,random_state = 1)

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.fit_transform(X_test)

from sklearn.tree import DecisionTreeClassifier
dtModel = DecisionTreeClassifier()
dtModel.fit(X_train, y_train)
dty_pred = dtModel.predict(X_test)


from sklearn.linear_model import LogisticRegression
lrModel = LogisticRegression()
lrModel.fit(X_train, y_train)
lry_pred = lrModel.predict(X_test)

from sklearn.naive_bayes import GaussianNB
nbModel = GaussianNB()
nbModel.fit(X_train, y_train)
nby_pred = nbModel.predict(X_test)

temp = []
for i,j,k in zip(dty_pred, lry_pred, nby_pred):
    temp.append([i, j, k])

y_pred = []
for l in temp:
    data = Counter(l)
    k = data.most_common(1)
    y_pred.append(k[0][0])

from sklearn.metrics import accuracy_score
Accuracy = accuracy_score(y_test, y_pred)
print("The Accuracy Score is: ",Accuracy)

with open('BreastCancerlr', 'wb') as f:
    pickle.dump(lrModel, f)

with open('BreastCancerdt', 'wb') as f:
    pickle.dump(dtModel, f)

with open('BreastCancernb', 'wb') as f:
    pickle.dump(nbModel, f)