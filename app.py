
from flask import Flask, render_template, request, url_for
import psycopg2          

app=Flask(__name__)

POSTGRESQL_URI= "postgres://vdpjeijz:6eDcYnTADXP0kJZ5KDxlAQK8ggFJjVP4@manny.db.elephantsql.com/vdpjeijz"

connection=psycopg2.connect(POSTGRESQL_URI)
try:
    with connection:
        with connection.cursor() as cursor: 
            cursor.execute(
                "CREATE TABLE transakcije (ime TEXT, prezime TEXT, donacija REAL);")
except psycopg2.errors.DuplicateTable:
    pass

@app.route('/')
def Index():
    return render_template("index.html")

@app.route('/doniraj',methods=['POST','GET'])
def doniraj():
    if request.method == "POST":
        print(request.form)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO transakcije VALUES(%s,%s,%s);",
                    (
                    request.form.get("ime"),
                    request.form.get("prezime"),
                    request.form.get("donacija"),
                ))
    return render_template("doniraj.html")


@app.route("/donacije")
def show_transakcije():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM transakcije;")
            transakcije=cursor.fetchall()
    return render_template("transakcije.html", unosi=transakcije)


if __name__=="__main__":
    app.run(debug=True)