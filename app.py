from flask import Flask, render_template, request, url_for,redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app=Flask(__name__)
#Dodavanje baze
app.secret_key="Tajni kljuc"

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///zaposlenici.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bp =SQLAlchemy(app)



class Zaposlenik(bp.Model):
    id=bp.Column(bp.Integer, primary_key=True)
    ime= bp.Column(bp.String(100),nullable=False)
    prezime=bp.Column(bp.String(100),nullable=False)
    datumrodenja= bp.Column(bp.String(100),nullable=False)
    spol=bp.Column(bp.String(100),nullable=False)
    kontakt=bp.Column(bp.String(100),nullable=False)
    odjel=bp.Column(bp.String(100),nullable=False)
    titula= bp.Column(bp.String(100),nullable=False)
    datumzaposlenja=bp.Column(bp.String(100),nullable=False)
    datumupisa=bp.Column(bp.String(30),nullable=False)

    def __init__(self,ime,prezime,datumrodenja,spol, kontakt,odjel,titula,datumzaposlenja,datumupisa):
        self.ime= ime
        self.prezime = prezime
        self.datumrodenja = datumrodenja
        self.spol= spol
        self.kontakt=kontakt
        self.odjel=odjel
        self.titula= titula
        self.datumzaposlenja=datumzaposlenja
        self.datumupisa=datumupisa



@app.route('/')
def Index():
    return redirect(url_for('doniraj'))

@app.route('/doniraj',methods=['POST','GET'])
def doniraj():
    if request.method=='POST':
        ime= request.form['ime']
        prezime= request.form['prezime']
        datumrodenja= request.form['datumrodenja']
        spol=request.form['spol']
        kontakt=request.form['kontakt']
        odjel=request.form['odjel']
        titula=request.form['titula']
        datumzaposlenja=request.form['datumzaposlenja']
        ct = datetime.now()
        datumupisa=ct
        podaci=Zaposlenik(ime,prezime,datumrodenja,spol,kontakt,odjel,titula,datumzaposlenja,datumupisa)
        bp.session.add(podaci)
        bp.session.commit()
                         
    return render_template("doniraj.html")


@app.route("/donacije")
def show_transakcije():
    svi_podaci= Zaposlenik.query.all()
    return render_template("transakcije.html", unosi=svi_podaci)



@app.route('/update/<id>', methods=['POST','GET']) 
def update(id):
    podac= Zaposlenik.query.get(id)
    return render_template ("update.html",unos=podac)   
    
@app.route('/updated/<id>',methods=['POST','GET'])
def updated(id):   
    if request.method=="POST":
        unos= Zaposlenik.query.get(id)
        unos.ime=request.form['ime']
        unos.prezime=request.form['prezime']
        unos.datumrodenja=request.form['datumrodenja']
        unos.spol=request.form['spol']
        unos.kontakt=request.form['kontakt']
        unos.odjel=request.form['odjel']
        unos.titula=request.form['titula']
        unos.datumzaposlenja=request.form['datumzaposlenja']
        ct = datetime.now()
        unos.datumupisa=ct 
        bp.session.commit()
        return redirect(url_for('show_transakcije'))

@app.route('/delete/<id>', methods=['GET','POST'])
def delete(id):
    podaci= Zaposlenik.query.get(id)
    bp.session.delete(podaci)
    bp.session.commit()
    

    return render_template('obrisano.html')


if __name__=="__main__":
    app.run(debug=True)