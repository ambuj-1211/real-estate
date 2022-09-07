from crypt import methods
import pickle
from flask import Flask,render_template,request,redirect,url_for
import numpy as np
app = Flask(__name__)
pmodel=pickle.load(open('model.pkl','rb'))
# enc = pickle.load(open('encoder.pkl','rb'))
@app.route('/')
###A list input all input values
#a variable predict containing predicted values of model.pred(intput)
def hello():
    return render_template('index.html')

@app.route('/show/<int:score>')
def show(score):
    return render_template('show.html',prediction=score)

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        locality_lable=float(request.form['lname'])
        typee=float(request.form['tname'])
        latitude=float(request.form['laname'])
        longitude=float(request.form['loname'])
        lease_type=float(request.form['lename'])
        gym=float(request.form['gname'])
        lift=float(request.form['liname'])
        swimming_pool=float(request.form['sname'])
        parking=float(request.form['pname'])
        property_size=float(request.form['prname'])
        bathroom=float(request.form['bname'])
        facing=float(request.form['fname'])
        water_supply=float(request.form['wname'])
        balconies=float(request.form['baname'])
        LIFT=float(request.form['liftname'])
        INTERNET=float(request.form['inname'])
        AC=float(request.form['acname'])
        INTERCOM=float(request.form['intername'])
        POOL=float(request.form['poname'])
        FS=float(request.form['fsname'])
        SECURITY=float(request.form['secname'])
        SC=float(request.form['scname'])
        PARK=float(request.form['parkname'])
        HK=float(request.form['hkname'])
        PB=float(request.form['pbname'])
    # locality_lable= enc.transform(list(locality_lable))
    prediction = pmodel.predict(np.array([[locality_lable,typee,latitude, longitude , lease_type,gym , lift , swimming_pool , parking, property_size,bathroom , facing , water_supply , balconies,LIFT,INTERNET,AC,INTERCOM,POOL,FS,SECURITY,SC,PARK,HK,PB]]))
    return redirect(url_for('show',score=prediction))

if __name__ == '__main__':
    app.run(debug=True)
