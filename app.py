from flask import Flask,render_template,request
import joblib
load_model=joblib.load('dib_acc82.pkl')
app=Flask(__name__)

@app.route('/') #Decorator
def welcome():
    return render_template('homepage.html')

@app.route('/predict', methods=['POST']) #Decorator
def predict():
    fname=request.form.get('firstname')
    lname=request.form.get('lastname')
    mob=request.form.get('mobilenumber')
    email=request.form.get('mail')
    print(fname,lname,mob,email)
    return render_template('homepage.html')


@app.route('/dia') #Decorator
def dia():
    return render_template('dia.html')

@app.route('/diapred', methods=['POST']) #Decorator
def diapred():
    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    test=request.form.get('test')
    mass=request.form.get('mass')
    pedi=request.form.get('pedi')
    age=request.form.get('age')
    print(preg,plas,pres,skin,test,mass,pedi,age)
    res=(load_model.predict([[preg,plas,pres,skin,test,mass,pedi,age]]))
    print('Class is predicted')
    if res[0]==1:
        val=('Diabetic')
        #return render_template('dia.html')
        #return 'Diabetic'
    else:
        val=('Non Diabetic')
        #return 'Non Diabetic'
    return render_template('result.html', value=val)

if __name__=='__main__':
    app.run(debug=True)