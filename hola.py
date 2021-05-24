from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
def url_principal():
	return render_template("template.html", nombre="Jorge Eduardo Estrada Gaytan")

@app.route("/ip/")
def dos_f():
	return render_template("ip.html")

@app.route("/pl/")
def tres_f():
	return render_template("pl.html")
@app.route("/el/")
def cuatro_f():
	return render_template("el.html")
@app.route("/pg/")
def cinco_f():
	return render_template("pg.html")

if __name__ == "__main__":
	app.run(debug=True)