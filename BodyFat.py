import pandas
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV

Data = pandas.read_csv('DataSets/BodyFat.csv')
Data = Data.drop(columns=['Density'])

Y = Data.BodyFat
X = Data.drop(columns=['BodyFat'])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=0)

# from sklearn.preprocessing import StandardScaler
# ss = StandardScaler()
# X_train = ss.fit_transform(X_train)
# X_test = ss.fit_transform(X_test)

# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# model.fit(X_train, y_train)

from sklearn.neural_network import MLPRegressor
model = MLPRegressor(hidden_layer_sizes = (150,), max_iter = 800)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(model.score(X_test, y_test))
print(X_test)
print(y_pred)
with open('BodyFat', 'wb') as f:
    pickle.dump(model, f)
plt.plot(model.loss_curve_)
plt.title("Loss Curve", fontsize=14)
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.show()

