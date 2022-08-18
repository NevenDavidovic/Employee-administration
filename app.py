from flask import Flask, render_template, request, url_for,redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from bp import bp,Zaposlenik
from flask import Blueprint
from sqlalchemy import func



app=Flask(__name__)



#Dodavanje baze
app.secret_key="Tajni kljuc"

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///zaposlenici.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bp.init_app(app)



@app.route('/')
def Index():
    return redirect(url_for('doniraj'))

@app.route('/doniraj',methods=['POST','GET'])
def doniraj():
    if request.method=='POST':
        ime= request.form['ime']
        prezime= request.form['prezime']
        datumr=request.form['datumrodenja']
        datumrodenja= datetime.strptime(datumr,'%Y-%m-%d')
        spol=request.form['spol']
        kontakt=request.form['kontakt']
        odjel=request.form['odjel']
        titula=request.form['titula']
        datum=request.form['datumzaposlenja']
        datumzaposlenja=datetime.strptime(datum,'%Y-%m-%d')
        
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
        datumro=request.form['datumrodenja']
        unos.datumrodenja=datetime.strptime(datumro,'%Y-%m-%d')
        unos.spol=request.form['spol']
        unos.kontakt=request.form['kontakt']
        unos.odjel=request.form['odjel']
        unos.titula=request.form['titula']
        datumzap=request.form['datumzaposlenja']
        unos.datumzaposlenja=datetime.strptime(datumzap,'%Y-%m-%d')
         
        bp.session.commit()
        return redirect(url_for('show_transakcije'))

@app.route('/delete/<id>', methods=['GET','POST'])
def delete(id):
    podaci= Zaposlenik.query.get(id)
    bp.session.delete(podaci)
    bp.session.commit()
    

    return redirect(url_for('show_transakcije'))

@app.route('/search', methods=['GET','POST'])
def search_all():
    if request.method== "POST":
       opcija=request.form['opcija']
       imes=request.form['imes'] 
       
       if opcija=="Ime":
        search_ime=Zaposlenik.query.filter_by(ime=imes).all()
        return render_template('search.html',unosi=search_ime)

       elif opcija=="Prezime":
        search_prezime=Zaposlenik.query.filter_by(prezime=imes).all()
        return render_template('search.html',unosi=search_prezime)
       elif opcija=="Odjel" :
        search_odjel=Zaposlenik.query.filter_by(odjel=imes)
        return render_template('search.html', unosi=search_odjel) 
  
    if request.method== "GET": 
        return render_template('search.html') 

@app.route('/statistika', methods=['GET','POST'])
def stats():
    
    muski=Zaposlenik.query.filter_by(spol="Muško").all()
    a=len(muski)
    zensko=Zaposlenik.query.filter_by(spol="Žensko").all()
    b=len(zensko)
    ortopedija=Zaposlenik.query.filter_by(odjel="Ortopedija").all()
    o=len(ortopedija)
    traumato=Zaposlenik.query.filter_by(odjel="Traumatologija").all()
    t=len(traumato)
    kirurgija=Zaposlenik.query.filter_by(odjel="Kirurgija").all()
    k=len(kirurgija)
    return render_template('statistika.html',muski=a, zenski=b,orto=o,trau=t, kir=k)
        

if __name__=="__main__":
    app.run(debug=True)