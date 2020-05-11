"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from ZivionFinalDSProject import app
from ZivionFinalDSProject.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines
from datetime import datetime
from flask import render_template



from datetime import datetime
from flask import render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import json 
import requests
import matplotlib.pyplot as plt

import io
import base64

from os import path

from flask import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError


from ZivionFinalDSProject.Models.QueryFormStructure import QueryFormStructure 
from ZivionFinalDSProject.Models.QueryFormStructure import LoginFormStructure 
from ZivionFinalDSProject.Models.QueryFormStructure import UserRegistrationFormStructure 

fifa = [
          {  "Belgium"},
          {  "France"},
          {  "Brazil"},
          {  "England"},
          {  "Uruguay"},
          {  "Croatia"},
          {  "Portugal"},
          {  "Spain"},
          {  "Argentina"},
          {  "Colombia"},
          {  "Mexico"},
          {  "Switzerland"},
          {  "Italy"},
          {  "Netherlands"},
          {  "Germany"},
          {  "Denmark"},
          {  "Sweden"},
          {  "Chile"},
          {  "Poland"},
          {  "Senegal"},
          {  "Peru"},
          {  "USA"},
          {  "Wales"},
          {  "Ukraine"},
          {  "Venezuela"},
          {  "Austria"},
          {  "Tunisia"},
          {  "Japan"},
          {  "Turkey"},
          {  "Serbia"},
          {  "Nigeria" },
          {  "Slovakia"},
          {  "IR Iran"},
          {  "Republic of Ireland"},
          {  "Algeria"},
          {  "Northern Ireland"},
          {  "Romania"},
          {  "Russia"},
          {  "Iceland"},
          {  "Korea Republic"},
          {  "Paraguay"},
          {  "Australia"},
          {  "Morocco"},
          {  "Norway"},
          {  "Czech Republic"},
          {  "Costa Rica"},
          {  "Ghana"},
          {  "Jamaica"},
          {  "Bosnia and Herzegovina"},
          {  "Scotland"},
          {  "Egypt"},
          {  "Hungary"},
          {  "Cameroon"},
          {  "Greece"},
          {  "Qatar"},
          {  "Mali" },
          {  "Congo DR"},
          {  "Finland"},
          {  "Bulgaria"},
          {  "Burkina Faso"},
          {  "Côte d'Ivoire"},
          {  "Honduras"},
          {  "Ecuador"},
          {  "Montenegro"},
          {  "Slovenia" },
          {  "Albania"},
          {  "Saudi Arabia"},
          {  "North Macedonia"},
          {  "El Salvador"},
          {  "Iraq"},
          {  "United Arab Emirates"},
          {  "South Africa"},
          {  "Canada"},
          {  "Guinea"},
          {  "Bolivia"},
          {  "China PR" },
          {  "Uganda"},
          {  "Cabo Verde"},
          {  "Syria"},
          {  "Curaçao"},
          {  "Panama"},
          {  "Oman"},
          {  "Gabon"},
          {  "Benin"},
          {  "Uzbekistan"},
          {  "Haiti"},
          {  "Belarus"},
          {  "Zambia"},
          {  "Congo"},
          {  "Lebanon"},
          {  "Georgia"},
          {  "Madagascar"},
          {  "Israel"},
          {  "Vietnam"},
          {  "Cyprus"},
          {  "Kyrgyz Republic"},
          {  "Jordan"},
          {  "Luxembourg"},
          {  "Bahrain"},
          {  "Mauritania"},
          {  "Libya"},
          {  "Armenia"},
          {  "Palestine"},
          {  "Estonia"},
          {  "Trinidad and Tobago"},
          {  "Mozambique"},
          {  "Kenya"},
          {  "India"},
          {  "Central African Republic"},
          {  "Faroe Islands"},
          {  "Zimbabwe"},
          {  "Niger"},
          {  "Thailand"},
          {  "Azerbaijan"},
          {  "Kosovo"},
          {  "Korea DPR"},
          {  "Namibia"},
          {  "Kazakhstan"},
          {  "Sierra Leone"},
          {  "Guinea-Bissau"},
          {  "Tajikistan"},
          {  "New Zealand"},
          {  "Malawi"},
          {  "Angola"},
          {  "Philippines"},
          {  "Antigua and Barbuda"},
          {  "Togo"},
          {  "Sudan"},
          {  "Turkmenistan"},
          {  "Guatemala"},
          {  "Rwanda"},
          {  "Lithuania"},
          {  "Comoros"},
          {  "Tanzania"},
          {  "Andorra"},
          {  "Myanmar"},
          {  "Latvia"},
          {  "Chinese Taipei"},
          {  "Lesotho"},
          {  "St. Kitts and Nevis"},
          {  "Suriname"},
          {  "Solomon Islands"},
          {  "Hong Kong"},
          {  "Yemen"},
          {  "Equatorial Guinea"},
          {  "Ethiopia"},
          {  "Kuwait"},
          {  "Botswana"},
          {  "Burundi"},
          {  "Afghanistan"},
          {  "Nicaragua"},
          {  "Liberia"},
          {  "Eswatini"},
          {  "Malaysia"},
          {  "Maldives"},
          {  "New Caledonia"},
          {  "Singapore"},
          {  "Dominican Republic"},
          {  "Grenada"},
          {  "Gambia"},
          {  "Tahiti"},
          {  "Barbados"},
          {  "Vanuatu"},
          {  "Fiji"},
          {  "Papua New Guinea"},
          {  "Guyana"},
          {  "St. Vincent and the Grenadines"},
          {  "Bermuda"},
          {  "South Sudan"},
          {  "Nepal"},
          {  "Belize"},
          {  "Mauritius"},
          {  "Indonesia"},
          {  "Cambodia"},
          {  "Moldova" },
          {  "St. Lucia"},
          {  "Chad"},
          {  "Puerto Rico"},
          {  "Cuba"},
          {  "Liechtenstein"},
          {  "São Tomé and Príncipe"},
          {  "Macau"},
          {  "Montserrat"},
          {  "Djibouti"},
          {  "Malta"},
          {  "Dominica"},
          {  "Bangladesh"},
          {  "Laos"},
          {  "Bhutan"},
          {  "Mongolia"},
          {  "Brunei Darussalam"},
          {  "American Samoa"},
          {  "Cayman Islands" },
          {  "Samoa" },
          {  "Bahamas"},
          {  "Timor-Leste"},
          {  "Gibraltar"},
          {  "Somalia"},
          {  "Guam"},
          {  "Pakistan"},
          {  "Aruba"},
          {  "Seychelles"},
          {  "Tonga"},
          {  "Turks and Caicos Islands"},
          {  "Eritrea"},
          {  "Sri Lanka"},
          {  "US Virgin Islands"},
          {  "British Virgin Islands"},
          {  "San Marino"},
          {  "Anguilla"},
]
a = pd.DataFrame(data=fifa, columns=['name'])
a1 = a.set_index(a.index+1)

logged = 0

###from DemoFormProject.Models.LocalDatabaseRoutines import IsUserExist, IsLoginGood, AddNewUser 

db_Functions = create_LocalDatabaseServiceRoutines() 

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            flash('Welcom - '+ form.FirstName.data + " " + form.LastName.data )
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        )

@app.route('/')
@app.route('/DataAnalyze1')
def DataAnalyze1():
    """Renders the home page."""
    return render_template(
        'DataAnalyze1.html',
        title='DataAnalyze1',
        year=datetime.now().year,
    )

@app.route('/')
@app.route('/DataAnalyze2')
def DataAnalyze2():
    """Renders the home page."""
    return render_template(
        'DataAnalyze2.html',
        title='DataAnalyze2',
        year=datetime.now().year,
    )



@app.route('/data2', methods=['GET', 'POST'])
def data2():
    form = QueryFormStructure(request.form)
    b1 = pd.read_csv(path.join(path.dirname(__file__), 'static', 'Data', 'data2.csv'))
    b1['USdollars'] = b1['USdollars'].astype(int) 
    b = b1.set_index(b1.index+1)  
    if (request.method == 'POST' and form.validate()):
        last2 = len(b)-1
        bb = b1.index[b1['Name'] == form.name.data].tolist()
        aa = a.index[a['name'] == form.name.data].tolist()
        imagePath = "/static/content/" + form.name.data + "2.png"
        if (len(bb) > 0 and len(aa) > 0):
            bbb = int(bb[0])
            aaa = int(aa[0])
            data222 = b.iloc[[1,bbb,last2]]
            plot = data222.plot(kind='bar',x='Name',y='USdollars')
            fig = plot.get_figure()
            fig.savefig("ZivionFinalDSProject" + imagePath)
            diffrencee = abs(bbb-aaa)
            if (diffrencee<=50):
                answerr = 'is'
            else:
                answerr = 'is not'


            return render_template(
            'DataAnalyze2.html', 
            year=datetime.now().year,
            form=form, 
            title='DataAnalyze2',
            repository_name='DataAnalyze2',
            data222 = b.iloc[bb],
            dataaa=a1.iloc[aa],
            image2 = imagePath,
            answer2 = answerr,
            diffrence2 = diffrencee,
            fifa = fifa,
            )
        else:
           flash('There Is No Such Country')
            # Here you should put what to do (or were to go) if registration was good
    return render_template(
        'data2.html',
        title='Data2',
        year=datetime.now().year,
        form=form,
        logged = logged,
        data = a1.iloc[0:6,0:1],
        dataa = a1.iloc[6:,0:1],
        data2 = b.iloc[0:6,1:4],
        data22 = b.iloc[6:,1:4]
     )


@app.route('/')
@app.route('/about')
def about():
    """Renders the home page."""
    if (isLoggedIn == 1) :
        return render_template(
            'about.html',
            title='about Page',
            year=datetime.now().year,
        )

@app.route('/')
@app.route('/contact')
def contact():
    """Renders the home page."""
    return render_template(
        'contact.html',
        title='contact Page',
        year=datetime.now().year,
    )

@app.route('/')
@app.route('/DataModel')
def DataModel():
    """Renders the home page."""
    return render_template(
        'DataModel.html',
        title='DataModel',
        year=datetime.now().year,
    )


@app.route('/data1', methods=['GET', 'POST'])
def data1():
    form = QueryFormStructure(request.form)
    x1  = pd.read_csv(path.join(path.dirname(__file__), 'static', 'Data', 'data1.csv'))
    x = x1.set_index(x1.index+1)
    if (request.method == 'POST' and form.validate()):
        last1 = len(x)-1
        xx = x1.index[x1['name'] == form.name.data].tolist()
        aa = a.index[a['name'] == form.name.data].tolist()
        imagePath = "/static/content/" + form.name.data + "1.png"
        if (len(xx) > 0 and len(aa) > 0):
            xxx = int(xx[0])
            aaa = int(aa[0])
            data111 = x.iloc[[0,xxx,last1]]
            plot = data111.plot.bar('name')
            fig = plot.get_figure()
            fig.savefig("ZivionFinalDSProject" + imagePath)
            diffrencee = abs(xxx-aaa)
            if (diffrencee<=50):
                answer = 'is'
            else:
                answer = 'is not'
            return render_template(
           'DataAnalyze1.html', 
            year=datetime.now().year,
            form=form, 
            title='DataAnalyze1',
            repository_name='DataAnalyze1',
            data111 = x.iloc[xx],
            dataaa=a1.iloc[aa],
            image1 = imagePath,
            answer1 = answer,
            diffrencee = diffrencee,
        
            )
        else:
           flash('There Is No Such Country')

    return render_template(
        'data1.html', 
        form=form, 
        title='Register New User',
        repository_name='Pandas',
        data = a1.iloc[0:6,0:1],
        dataa = a1.iloc[6:,0:1],
        data1 = x.iloc[0:6,0:6],
        data11 = x.iloc[6:,0:6],
        logged = logged,
        year=datetime.now().year,
        )

# -------------------------------------------------------
# Login page
# This page is the filter before the data analysis
# -------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def Login():
    global logged
    form = LoginFormStructure(request.form)
    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            logged = 1
            flash('Login approved!')
            #return redirect('<were to go if login is good!')
        else:
            logged = 0
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        )



