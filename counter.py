from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

app.secret_key = 'counterPy'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    session['count'] = session['count'] + 1
    print(session['count'])
    return render_template('index.html', count=session['count'])

@app.route('/countUp', methods=['POST'])
def counterUp():
    session['count'] = session['count'] + 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def restart():
    if session['count'] > 0:
    	session['count'] = 0
    return redirect('/')

@app.route('/destroy_session')
def destroy():
	session.clear()
	return redirect('/')

if __name__=="__main__":
    app.run(debug=True) 