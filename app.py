
from flask import flash
from flask import Flask, render_template, request, url_for,redirect
import psycopg2          
import datetime
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
#Dodavanje baze
app.secret_key="Tajni kljuc"

app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:''@localhost/zaposlenici'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bp =SQLAlchemy(app)



class Zaposlenik(bp.Model):
    id=bp.Column(bp.Integer, primary_key=True)
    ime= bp.Column(bp.String(100),nullable=False)
    prezime=bp.Column(bp.String(100),nullable=False)
    donacija= bp.Column(bp.Integer,nullable=False)

    def __init__(self,ime,prezime,donacija):
        self.ime= ime
        self.prezime = prezime
        self.donacija =donacija



@app.route('/')
def Index():
    return render_template("index.html")

@app.route('/doniraj',methods=['POST','GET'])
def doniraj():
    if request.method=='POST':
        ime= request.form['ime']
        prezime= request.form['prezime']
        donacija= request.form['donacija']

        podaci=Zaposlenik(ime,prezime,donacija)
        bp.session.add(podaci)
        bp.session.commit()
                         
    return render_template("doniraj.html")


@app.route("/donacije")
def show_transakcije():
    svi_podaci= Zaposlenik.query.all()
    return render_template("transakcije.html", unosi=svi_podaci)

@app.route('/update/<id>', methods=['GET','POST']) 
def azuriraj(id):
    if request.method=="POST":
        podaci= Zaposlenik.query.get(request.form.get(id))
        podaci.name= request.form['ime']
        podaci.prezime= request.form['prezime']
        podaci.donacija= request.form['donacija']

        bp.session.commit()
        flash("Ažuriran zaposlenik")
        return redirect(url_for('show_transakcije'))
    return render_template('update.html')

@app.route('/delete/<id>', methods=['GET','POST'])
def delete(id):
    podaci= Zaposlenik.query.get(id)
    bp.session.delete(podaci)
    bp.session.commit()
    

    return render_template('transakcije.html')


if __name__=="__main__":
    app.run(debug=True)