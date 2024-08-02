from flask import render_template, url_for, request, Blueprint, redirect, flash
import pickle

auth = Blueprint('auth', __name__)

@auth.route('/Diabetes', methods=['GET', 'POST'])
def Diabetes():
    if request.method == 'POST':
        Pregnencies = (request.form.get('Pregnencies', type=int))
        Glucose = (request.form.get('Glucose', type = int))
        BloodPressure = (request.form.get('BloodPressure', type = int))
        SkinThickness = (request.form.get('SkinThickness', type = int))
        Insulin = (request.form.get('Insulin', type = int))
        bmi = (request.form.get('BMI', type = float))
        DiabetesPedigreeFunction = (request.form.get('DiabetesPedigreeFunction', type = float))
        Age = (request.form.get('Age', type = int))

        inputs = [[Pregnencies, Glucose, BloodPressure, SkinThickness, Insulin, bmi, DiabetesPedigreeFunction, Age]]
        print(inputs)

        with open('/home/emmaykoushal/Documents/ML_PROJECT/Models/DiabetesModel', 'rb') as f:
            model = pickle.load(f)
        prediction = model.predict(inputs)
        print(prediction)
        if (prediction[0] == 1):
            return redirect(url_for('views.DiabetesOne'))
        else:
            return redirect(url_for('views.DiabetesZero'))

        
    return render_template('Diabetes.html')

@auth.route('/Heart', methods=['GET', 'POST'])
def Heart():
    if request.method == 'POST':
        Age = (request.form.get('Age', type=int))
        Sex = (request.form.get('Sex', type = int))
        ChestPainType = (request.form.get('ChestPainType', type = int))
        RestingBloodPressure = (request.form.get('RestingBloodPressure', type = int))
        SerumCholestoral = (request.form.get('SerumCholestoral', type = int))
        FastingBloodSugar = (request.form.get('FastingBloodSugar', type = int))
        RestingElectroDiagraphicResults = (request.form.get('RestingElectroDiagraphicResults', type = int))
        MaximumHeartRate = (request.form.get('MaximumHeartRate', type = int))
        ExerciseIndusedAngina = (request.form.get('ExerciseIndusedAngina', type = int))
        OldPeak = (request.form.get('OldPeak', type = float))
        Slope = (request.form.get('Slope', type = int))
        NoofMajorVessels = (request.form.get('NoofMajorVessels', type = int))
        Thal = (request.form.get('Thal', type = int))

        inputs = [[Age, Sex, ChestPainType, RestingBloodPressure, SerumCholestoral, FastingBloodSugar, 
                    RestingElectroDiagraphicResults, MaximumHeartRate, ExerciseIndusedAngina, OldPeak, Slope, NoofMajorVessels, Thal]]
        print(inputs)

        with open('/home/emmaykoushal/Documents/ML_PROJECT/Models/Heart', 'rb') as f:
            model = pickle.load(f)
        prediction = model.predict(inputs)
        print(prediction)
        if (prediction[0] == 1):
            return redirect(url_for('views.HeartOne'))
        else:
            return redirect(url_for('views.HeartZero'))

        
    return render_template('Heart.html')

@auth.route('/BodyFat', methods=['GET', 'POST'])
def BodyFat():
    if request.method == 'POST':
        Age = (request.form.get('Age', type=int))
        Weight = (request.form.get('Weight', type = float))
        Height = (request.form.get('Height', type = float))
        Neck = (request.form.get('Neck', type = float))
        Chest = (request.form.get('Chest', type = float))
        Abdomen = (request.form.get('Abdomen', type = float))
        Hip = (request.form.get('Hip', type = float))
        Thigh = (request.form.get('Thigh', type = float))
        Knee = (request.form.get('Knee', type = float))
        Ankle = (request.form.get('Ankle', type = float))
        Biceps = (request.form.get('Biceps', type = float))
        ForeArm = (request.form.get('ForeArm', type = float))
        Wrist = (request.form.get('Wrist', type = float))

        inputs = [[Age, Weight, Height, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, ForeArm, Wrist]]
        print(inputs)

        with open('/home/emmaykoushal/Documents/ML_PROJECT/Models/BodyFat', 'rb') as f:
            model = pickle.load(f)
        prediction = model.predict(inputs)
        print(prediction)
        if (prediction[0] > 2 and prediction[0] < 4):
            return redirect(url_for('views.EssentialFat', fat = prediction))
        elif (prediction[0] > 6 and prediction[0] < 13):
            return redirect(url_for('views.Athletes', fat = prediction))
        else:
            return redirect(url_for('views.Obese', fat = prediction))
        
    return render_template('BodyFat.html')

@auth.route('/BreastCancer', methods=['GET', 'POST'])
def BreastCancer():
    if request.method == 'POST':
        RadiusMean = (request.form.get('RadiusMean', type=float))
        TextureMean= (request.form.get('TextureMean', type = float))
        PerimeterMean = (request.form.get('PerimeterMean', type = float))
        AreaMean = (request.form.get('AreaMean', type = float))
        PerimeterSe = (request.form.get('PerimeterSe', type = float))
        AreaSe = (request.form.get('AreaSe', type = float))
        RadiusWorst = (request.form.get('RadiusWorst', type = float))
        

        inputs = [[RadiusMean, TextureMean, PerimeterMean, AreaMean, PerimeterSe, AreaSe, RadiusWorst]]
        print(inputs)

        with open('/home/emmaykoushal/Documents/ML_PROJECT/Models/BreastCancerdt', 'rb') as f1:
            model1 = pickle.load(f1)
        with open('/home/emmaykoushal/Documents/ML_PROJECT/Models/BreastCancerlr', 'rb') as f2:
            model2 = pickle.load(f2)
        with open('/home/emmaykoushal/Documents/ML_PROJECT/Models/BreastCancernb', 'rb') as f3:
            model3 = pickle.load(f3)
        

        p1 = model1.predict(inputs)
        p2 = model2.predict(inputs)
        p3 = model3.predict(inputs)

        predictions = [p1[0], p2[0], p3[0]]
        output = max(set(predictions), key = predictions.count)
        print(output)

        if (output == 1):
            return redirect(url_for('views.BreastCancerOne'))
        else:
            return redirect(url_for('views.BreastCancerZero'))

    return render_template('BreastCancer.html')
