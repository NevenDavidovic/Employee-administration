
from flask import Flask, render_template, request, url_for
import psycopg2          

app=Flask(__name__)
transakcije=[]


@app.route('/')
def Index():
    return render_template("index.html")

@app.route('/doniraj',methods=['POST','GET'])
def doniraj():
    if request.method == "POST":
        print(request.form)
        transakcije.append(
            (
            request.form.get("ime"),
            request.form.get("prezime"),
            request.form.get("donacija"),
            )
        )
    return render_template("doniraj.html")


@app.route("/donacije")
def show_transakcije():
    return render_template("transakcije.html", unosi=transakcije)


if __name__=="__main__":
    app.run(debug=True)