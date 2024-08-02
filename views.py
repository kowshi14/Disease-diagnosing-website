from flask import Blueprint, render_template, request, redirect, url_for
from .Fats import EssentialFat
from .Fats import Athletes
from .Fats import Obese

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/DiabetesOne')
def DiabetesOne():
    return render_template('DiabetesOne.html')

@views.route('/DiabetesZero')
def DiabetesZero():
    return render_template('DiabetesZero.html')

@views.route('/HeartOne')
def HeartOne():
    return render_template('HeartOne.html')

@views.route('/HeartZero')
def HeartZero():
    return render_template('HeartZero.html')

@views.route('/EssentialFat/<fat>')
def EssentialFat(fat):
    return render_template('EssentialFat.html', fat=fat)

@views.route('/Athletes/<fat>')
def Athletes(fat):
    return render_template('Athletes.html', fat=fat)

@views.route('/Obese/<fat>')
def Obese(fat):
    return render_template('Obese.html', fat=fat)

@views.route('/BreastCancerOne')
def BreastCancerOne():
    return render_template('BreastCancerOne.html')

@views.route('/BreastCancerZero')
def BreastCancerZero():
    return render_template('BreastCancerZero.html')