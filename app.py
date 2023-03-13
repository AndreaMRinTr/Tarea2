from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username[0].isupper() and password.isalnum():
            return redirect('/login/success')
        else:
            return redirect('/login')
    else:
        return render_template('login.html')

@app.route('/login/success')
def success():
    return 'Login successful!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)
