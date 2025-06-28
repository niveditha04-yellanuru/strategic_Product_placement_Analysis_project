from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy credentials
EMAIL = "admin@example.com"
PASSWORD = "admin123"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['email'] == EMAIL and request.form['password'] == PASSWORD:
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid Credentials")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/story')
def story():
    return render_template('story.html')

if __name__ == '__main__':
    app.run(debug=True)
