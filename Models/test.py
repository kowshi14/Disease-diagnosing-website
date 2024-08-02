import pickle

with open('/home/emmaykoushal/Documents/ML_PROJECT/Models/DiabetesModel92', 'rb') as f:
    model = pickle.load(f)

inputs = [[1, 96, 122, 0, 0, 22.4, 0.21, 27]]
print(model.predict(inputs))