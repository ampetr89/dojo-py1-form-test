from flask import Flask, render_template, request, redirect, session # learning a new thing

app = Flask(__name__)

secret_key = open('secret-key.txt', 'r').read().strip()
app.secret_key = secret_key

@app.route('/')
def index():
	# print('youre on the index')
	return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
	print ("received posted form info")
	print(request.form)
	session['name'] = request.form['name']
	session['email'] = request.form['email']
	session['tel'] = request.form['tel']
	return redirect('/show')

@app.route('/show')
def show_user():
	print(session)
	return render_template('user.html', name=session['name'],
		email=session['email'], tel=session['tel'])


app.run(debug=True)