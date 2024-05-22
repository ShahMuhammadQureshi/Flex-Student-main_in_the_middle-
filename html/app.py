from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# User data for demonstration purposes
users = {
    '21K-4755': 'password123'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    print("Received username:", username)
    print("Received password:", password)
    
    if username in users and users[username] == password:
        # Redirect to a success page if login is successful
        return redirect(url_for('success'))
    else:
        # Redirect back to login page with an error message
        return render_template('index.html', error='Invalid username or password')

@app.route('/success')
def success():
    return 'Login Successful!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
    #app.run(debug=True, host='0.0.0.0')

