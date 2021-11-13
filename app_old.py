from flask import Flask,render_template
app=Flask(__name__)
'''
/ : Welcome to home page
/gallary : Welcome to Gallary
/contact : Welcome to contact page
/enquiry : Welcome to enquiry page
/login : Welcome to login page
'''
@app.route('/') #Decorator
def welcome():
    return 'Welcome to Home page'

@app.route('/homepage') #Decorator
def index():
    return render_template('homepage.html')

@app.route('/gallary') #Decorator
def fun1():
    return 'Welcome to Gallary'

@app.route('/contact') #Decorator
def fun2():
    return 'Welcome to Contact page'

@app.route('/enquiry') #Decorator
def fun3():
    return 'Welcome to enquiry page'

@app.route('/login') #Decorator
def fun4():
    return 'Welcome to login page'

@app.route('/hi') #Decorator
def hi():
    return 'Hey, Hi'

app.run(debug=True)