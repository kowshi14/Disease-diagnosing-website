import pandas
import pickle

Data = pandas.read_csv('DataSets/heart.csv')

Y = Data.target
X = Data.drop(columns = ['target'])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1, random_state = 1)

# from sklearn.preprocessing import StandardScaler
# ss = StandardScaler()
# X_train = ss.fit_transform(X_train)
# X_test = ss.fit_transform(X_test)

from sklearn.neural_network import MLPClassifier
model = MLPClassifier(max_iter=500, activation='relu', hidden_layer_sizes = (150, 100))
print(model)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(X_test)
print(y_pred)
from sklearn.metrics import accuracy_score
Accuracy = accuracy_score(y_test, y_pred)
print("The Accuracy Score is: ",Accuracy)

with open('Heart', 'wb') as f:
    pickle.dump(model, f)