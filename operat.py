# -*- coding: utf-8 -*-
import os
import sqlite3
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory, g, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'temp_uploads'
ALLOWED_EXTENSIONS = {'txt', 'dxf'}
DATABASE = '//roboty.sqlite3'
secret_key='adam'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///roboty.sqlite3'
app.config['SECRET_KEY'] = secret_key
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db.Model.metadata.reflect(db.engine)
class Roboty(db.Model):
    __tablename__='roboty'
    __table_args__={'extend_existing':True}
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idpracy = db.Column(db.String(15), unique=True, nullable=True)
    wojew = db.Column(db.String(50), unique=False, nullable=False)
    powiat = db.Column(db.String(30), unique=False, nullable=False)
    jdnewid = db.Column(db.String(100), unique=False, nullable=False)
    obreb = db.Column(db.String(100), unique=False, nullable=False)
    obiekt = db.Column(db.String(80), unique=False, nullable=False)
    dzialki = db.Column(db.String(80), unique=False, nullable=False)
    


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nowa_robota', methods = ['GET', 'POST'])
def nowa_robota():
     if request.method == 'POST':
        ident=request.form['idpracy']
        woj=request.form['wojew']
        pow=request.form['powiat']
        jew=request.form['jdnewid']
        obr=request.form['obreb']
        ob=request.form['obiekt']
        dz=request.form['dzialki']
        nowarobota=Roboty(idpracy=ident, wojew=woj, powiat=pow, jdnewid=jew, obreb=obr, obiekt=ob, dzialki=dz)
        db.session.add(nowarobota)
        db.session.commit()
        flash('Record was successfully added')
        return redirect(url_for('przeglad'))
     return render_template('nowa_robota.html')

@app.route('/przeglad')
def przeglad():
    lista_prac = Roboty.query.all()
    return render_template('przeglad.html', lista=lista_prac)

@app.route('/roboty/<slug>')
def szczegoly(slug):
    robota =Roboty.query.filter_by(idpracy=slug).first()
    return render_template('szczegoly.html', robota=robota)

@app.route('/generuj', methods = ['GET', 'POST'])
def generuj():
    lista_prac=Roboty.query.all()
    return render_template('generuj.html', lista=lista_prac) 

@app.route('/sprawozdanie', methods = ['GET', 'POST'])
def sprawozdanie():
    rob_select = request.form.get('rob')
    rob=Roboty.query.filter_by(idpracy=rob_select).first()
    return render_template('sprawozdanie.html', rob=rob)

@app.route('/raport', methods = ['GET', 'POST'])
def raport():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        data = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename), sep='\t', header=None )
        rob_select = request.form.get('rob')
        rob=Roboty.query.filter_by(idpracy=rob_select).first()
    return render_template('raport.html', rob=rob, wynik=[data.to_html(header=False, border=0, index_names=False, bold_rows=False )])
    
if __name__ == '__main__':
    app.run(debug=True) 
    
