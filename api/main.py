from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates")

@app.route('/')
def start():
	return render_template('one.html')

@app.route('/quotes')
def quotes():
	return render_template('quote.html')
