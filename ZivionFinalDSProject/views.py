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
#הקוד הופך את הרשימה לדטא פריים ולשנות את האינדקס לדירוג רגיל ולא דירוג בשפת מחשב
a = pd.DataFrame(data=fifa, columns=['name'])
a1 = a.set_index(a.index+1)
#________________________________________________________________________________________________________________________
#הגדרת משתנה שבהמשך יזהה האם המשתמש מחובר
logged = 0
#________________________________________________________________________________________________________________________
db_Functions = create_LocalDatabaseServiceRoutines() 
#________________________________________________________________________________________________________________________
#פונקציה הפותחת את עמוד הבית 
@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title='Home Page',
    )
#________________________________________________________________________________________________________________________
#פונקציה הפותחת את עמוד הדטא מודל 
@app.route('/')
@app.route('/DataModel')
def DataModel():
    """Renders the home page."""
    return render_template(
        'DataModel.html',
        title='DataModel',
        year=datetime.now().year,
    )
#________________________________________________________________________________________________________________________
#פונקציה הפותחת את עמוד האבוט 
@app.route('/')
@app.route('/about')
def about():
    """Renders the home page."""
    return render_template(
        'about.html',
        title='about Page',
        year=datetime.now().year,
        )
#________________________________________________________________________________________________________________________
#פונקציה הפותחת את עמוד המידע הראשון 
@app.route('/data1', methods=['GET', 'POST'])
def data1():
    ## קורא לפורם
    form = QueryFormStructure(request.form)
    ##לדטא פריים csvהופך את קובץ ה
    x1  = pd.read_csv(path.join(path.dirname(__file__), 'static', 'Data', 'data1.csv'))
    ##הופך את האינדקס מדירוג של שפת מחשב לדירוג רגיל 
    x = x1.set_index(x1.index+1)
    ## הפונקציה בודקת האם המשתמש הכניס ערך לפורם ובמידה וכן עושה את הדברים הבאים
    if (request.method == 'POST' and form.validate()):
        ##הפונקציה מאתרת את האינדקס של המדינה האחרונה בבסיס הנתונים
        last1 = len(x)-1
        ## בודק מה אינדקס של הערך ההוכנס בשני בסיסי הנתונים ומבודד את הנתונים שלו מהדטא בייס בתור רשימה 
        xx = x1.index[x1['name'] == form.name.data].tolist()
        aa = a.index[a['name'] == form.name.data].tolist()
        ##קובע את הנתיב ושם הקובץ שבו התמונה תישמר  
        imagePath = "/static/content/" + form.name.data + "1.png"
        ##  בודק האם אורך הרשימה גדול מאפס. בכך בעצם בודק האם הערך ההוכנס הוא מדינה הנמצאת בשתי בסיסי הנתונים
        ## מפני שבמידה והערך שהוכנס אינו מדינה הנמצאת בשתי בסיסי הנתונים אז הרשימה היתה ריקה משמע שהאורך שלה היה שווה לאפס
        if (len(xx) > 0 and len(aa) > 0):
            ## הופך את האינדקס של הערך שהוכנס (בשתי בסיסי הנתונים) לאינט
            xxx = int(xx[0])
            aaa = int(aa[0])
            ## יוצר דאטא פריים של הנתונים של המדינה הראשונה, האחרונה והמדינה שבחר השמתמש 
            data111 = x.iloc[[0,xxx,last1]]
            ## יוצר גרף מהדטא הפריים שנוצר בשורה הקודמת
            plot = data111.plot.bar('name')
            ## שומר את הגרף כתמונה 
            fig = plot.get_figure()
            fig.savefig("ZivionFinalDSProject" + imagePath)
            ##הפונקציה מגיעה למסקנה האם יש קשר בין רמת ההישגים הלימודיים במדינה לבין רמת הכדורגל בהתבסס על הנתונים מהמדינה הספציפית שבחר המשתמש
            ## הפונקציה מחשבת את ההפרש בין האינדקסים של המדינה שהוכנסה על ידי המשתמש בשתי בסיסי הנתונים
            diffrencee = abs(xxx-aaa)
            ##הפונקציה עושה שאם ההפרש בין האינדקסים שווה או קטן מ50 אז התשובה שיש (הכוונה ליש קשר...) ואם לא אז אין
            if (diffrencee<=50):
                answer = 'is'
            else:
                answer = 'is not'
            ## הפונקציה פותחת את דף הדאטא אנלייז 
            return render_template(
           'DataAnalyze1.html', 
            year=datetime.now().year,
            form=form, 
            title='DataAnalyze1',
            repository_name='DataAnalyze1',
            ## עושה דאטא פריים חדש המציג את ההישגים הלימודיים של המדינה אותה הכניס המשתמש
            data111 = x.iloc[xx],
            ## עושה דאטא פריים חדש המציג את נתוני רמת הכדוגל של המדינה אותה הכניס המשתמש
            dataaa=a1.iloc[aa],
            ## נותן למשתנים הבאים שם כדי שיהיה אפשר להשתמש באם בקובץ האייץ טי אם אל
            image1 = imagePath,
            answer1 = answer,
            diffrencee = diffrencee,
        
            )
        ##אם המשתמש מכניס מדינה שלא נמצאת בשתי בסיסי הנתונים,לא רשומה באות גדולה או לא קיימת אז הפונקציה מחזירה לו הודעה האומרת שאין כזו מדינה 
        else:
           flash('There Is No Such Country')
    ## פונקציה הפותחת את עמוד המידע הראשון
    return render_template(
        'data1.html', 
        form=form, 
        title='Register New User',
        repository_name='Pandas',
        ## עושה דאטא פריים המציג את רמת הכדורגל של 6 המדינות הראשונות
        data = a1.iloc[0:6,0:1],
        ## עושה דאטא פריים המציג את רמת הכדורגל של שאר המדינות
        dataa = a1.iloc[6:,0:1],
        ## עושה דאטא פריים המציג את רמת ההשכלה של 6 המדינות הראשונות
        data1 = x.iloc[0:6,0:6],
        ## עושה דאטא פריים המציג את רמת ההשכלה של שאר המדינות
        data11 = x.iloc[6:,0:6],
        ## נותן למשתנה הבא שם כדי שיהיה אפשר להשתמש בו בקובץ האייץ טי אם אל
        logged = logged,
        year=datetime.now().year,
        )
#________________________________________________________________________________________________________________________
## פונקציה הפותחת את עמוד הניתוח דטא הראשון
@app.route('/')
@app.route('/DataAnalyze1')
def DataAnalyze1():
    """Renders the home page."""
    return render_template(
        'DataAnalyze1.html',
        title='DataAnalyze1',
        year=datetime.now().year,
    )
#________________________________________________________________________________________________________________________
#פונקציה הפותחת את עמוד המידע השני 
@app.route('/data2', methods=['GET', 'POST'])
def data2():
    ## קורא לפורם
    form = QueryFormStructure(request.form)
    ##לדטא פריים csvהופך את קובץ ה
    b1 = pd.read_csv(path.join(path.dirname(__file__), 'static', 'Data', 'data2.csv'))
    ## הופך את המידע בבסיס הנתונים בעמודה בשם "דולרים אמריקאים" למשתנה מסוג אינט
    b1['USdollars'] = b1['USdollars'].astype(int) 
    ##הופך את האינדקס מדירוג של שפת מחשב לדירוג רגיל
    b = b1.set_index(b1.index+1)
    ## הפונקציה בודקת האם המשתמש הכניס ערך לפורם ובמידה וכן עושה את הדברים הבאים
    if (request.method == 'POST' and form.validate()):
        ## הפונקציה מאתרת את האינדקס של המדינה האחרונה בבסיס הנתונים
        last2 = len(b)-1
        ## בודק מה אינדקס של הערך ההוכנס בשני בסיסי הנתונים ומבודד את הנתונים שלו מהדטא בייס בתור רשימה 
        bb = b1.index[b1['Name'] == form.name.data].tolist()
        aa = a.index[a['name'] == form.name.data].tolist()
        ## קובע את הנתיב ושם הקובץ שבו התמונה תישמר
        imagePath = "/static/content/" + form.name.data + "2.png"
        ##  בודק האם אורך הרשימה גדול מאפס. בכך בעצם בודק האם הערך ההוכנס הוא מדינה הנמצאת בשתי בסיסי הנתונים
        ## מפני שבמידה והערך שהוכנס אינו מדינה הנמצאת בשתי בסיסי הנתונים אז הרשימה היתה ריקה משמע שהאורך שלה היה שווה לאפס
        if (len(bb) > 0 and len(aa) > 0):
            ## הופך את האינדקס של הערך שהוכנס (בשתי בסיסי הנתונים) לאינט
            bbb = int(bb[0])
            aaa = int(aa[0])
            ## יוצר דאטא פריים של הנתונים של המדינה הראשונה, האחרונה והמדינה שבחר המשתמש 
            data222 = b.iloc[[1,bbb,last2]]
            ## יוצר גרף מהדטא הפריים שנוצר בשורה הקודמת
            plot = data222.plot(kind='bar',x='Name',y='USdollars')
            fig = plot.get_figure()
            ## שומר את הגרף כתמונה 
            fig.savefig("ZivionFinalDSProject" + imagePath)
            ## הפונקציה מגיעה למסקנה האם יש קשר בין רמת ההישגים הלימודיים במדינה לבין רמת הכדורגל בהתבסס על הנתונים מהמדינה הספציפית שבחר המשתמש
            ## הפונקציה מחשבת את ההפרש בין האינדקסים של המדינה שהוכנסה על ידי המשתמש בשתי בסיסי הנתונים
            diffrencee = abs(bbb-aaa)
            ##הפונקציה עושה שאם ההפרש בין האינדקסים שווה או קטן מ50 אז התשובה שיש (הכוונה ליש קשר...) ואם לא אז אין
            if (diffrencee<=50):
                answerr = 'is'
            else:
                answerr = 'is not'
            ## הפונקציה פותחת את דף הדאטא אנלייז
            return render_template(
            'DataAnalyze2.html', 
            year=datetime.now().year,
            form=form, 
            title='DataAnalyze2',
            repository_name='DataAnalyze2',
            ## עושה דאטא פריים חדש המציג את הנתונים הפיננסים של המדינה אותה הכניס המשתמש
            data222 = b.iloc[bb],
            ## עושה דאטא פריים חדש המציג את נתוני רמת הכדוגל של המדינה אותה הכניס המשתמש
            dataaa = a1.iloc[aa],
            ## נותן למשתנים הבאים שם כדי שיהיה אפשר להשתמש באם בקובץ האייץ טי אם אל
            image2 = imagePath,
            answer2 = answerr,
            diffrence2 = diffrencee,
            fifa = fifa,
            )
        ##אם המשתמש מכניס מדינה שלא נמצאת בשתי בסיסי הנתונים,לא רשומה באות גדולה או לא קיימת אז הפונקציה מחזירה לו הודעה האומרת שאין כזו מדינה 
        else:
           flash('There Is No Such Country')
    ## פונקציה הפותחת את עמוד המידע הראשון
    return render_template(
        'data2.html',
        title='Data2',
        year=datetime.now().year,
        form=form,
        ## נותן למשתנה הבא שם כדי שיהיה אפשר להשתמש בו בקובץ האייץ טי אם אל
        logged = logged,
        ## עושה דאטא פריים המציג את רמת הכדורגל של 6 המדינות הראשונות
        data = a1.iloc[0:6,0:1],
        ## עושה דאטא פריים המציג את רמת הכדורגל של שאר המדינות
        dataa = a1.iloc[6:,0:1],
        ## עושה דאטא פריים המציג את רמת ההשכלה של 6 המדינות הראשונות
        data2 = b.iloc[0:6,1:4],
        ## עושה דאטא פריים המציג את רמת ההשכלה של שאר המדינות
        data22 = b.iloc[6:,1:4]
     )
#________________________________________________________________________________________________________________________
## פונקציה הפותחת את עמוד הניתוח דטא השני
@app.route('/')
@app.route('/DataAnalyze2')
def DataAnalyze2():
    return render_template(
        'DataAnalyze2.html',
        title='DataAnalyze2',
        year=datetime.now().year,
    )
#________________________________________________________________________________________________________________________
@app.route('/login', methods=['GET', 'POST'])
def Login():
    ## הופך את המשתנה הבא לשמיש בכל פונקציה
    global logged
    ## קורא לפורם
    form = LoginFormStructure(request.form)
    ## הפונקציה בודקת האם המשתמש הכניס ערך לפורם שתואם להגבלות ובמידה וכן עושה את הדברים הבאים
    if (request.method == 'POST' and form.validate()):
        ## בודק האם הערכים שהכניס המשתמש נכונים ובאמת יש לו משתמש באתר
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            ## מגדיר את הערך לוגד שווה ל-1
            ## ערך זה עוזר לבדוק אם המשתמש מחובר ובמידה וכן מאשר לו לנתח מידע
            logged = 1
            ## מקפיץ לו הודעה שאומרת לו שהתחבר בהצלחה
            flash('Login approved!')
        ## אם הערכים שהכניס המשתמש לא נכונים הפונקציה עושה את הדברים הבאים 
        else:
            ## מגדיר את הערך לוגד שווה ל-01
            ## ערך זה עוזר לבדוק אם המשתמש מחובר ובמידה וכן מאשר לו לנתח מידע
            logged = 0
            ## מקפיץ לו הודעה שאומרת לו שהכניס פרטים לא נכונים
            flash('Error in - Username and/or password')
    ## פונקציה הפותחת את עמוד ההתחברות
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        )
#________________________________________________________________________________________________________________________
@app.route('/register', methods=['GET', 'POST'])
def register():
    ## קורא לפורם
    form = UserRegistrationFormStructure(request.form)
    ## הפונקציה בודקת האם המשתמש הכניס ערך לפורם שתואם להגבלות ובמידה וכן עושה את הדברים הבאים
    if (request.method == 'POST' and form.validate()):
        ## בודק האם הערכים שהכניס המשתמש לא נמצאים במאגר המשתמשים ואין לו באמת משתמש
        if (not db_Functions.IsUserExist(form.username.data)):
            ## מוסיף את הפרטים שהכניס המתשתמש לקובץ הסויסי
            db_Functions.AddNewUser(form)
            ## מקפיץ למשתמש הודעה שאומרת ברוך הבאה ואת השם הפרטי והמשפחה של המשתמש
            flash('Welcom - '+ form.FirstName.data + " " + form.LastName.data )
        ## אם הערכים שהכניס המשתמש נמצאים במאגר ויש לו משתמש
        else:
            ## מקפיץ למשתמש הודעה שאומרת שמשתמש עם שם כזה כבר קיים ואומרת את שם המשתמש
            flash('Error: User with this Username already exist ! - '+ form.username.data)
    ## פונקציה הפותחת את עמוד ההרשמה
    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        )
#________________________________________________________________________________________________________________________
## פונקציה הפותחת את עמוד יצירת קשר
@app.route('/')
@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title='contact Page',
        year=datetime.now().year,
    )
#________________________________________________________________________________________________________________________