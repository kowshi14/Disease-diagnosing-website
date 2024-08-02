import pandas
import pickle

Data  = pandas.read_csv('DataSets/Diabetes.csv')
print(Data.head())

from sklearn.model_selection import train_test_split
Y = Data.Outcome
X = Data.drop(columns = ['Outcome'])

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.05, random_state = 0)

# from sklearn.preprocessing import StandardScaler
# ss = StandardScaler()
# X_train = ss.fit_transform(X_train)
# X_test = ss.fit_transform(X_test)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(X_test)
print(y_pred)
from sklearn.metrics import accuracy_score
Accuracy = accuracy_score(y_test, y_pred)
print("The Accuracy Score is: ",Accuracy)


with open('DiabetesModel', 'wb') as f:
    pickle.dump(model, f)
