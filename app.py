from crypt import methods
import pickle
from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)
pmodel=pickle.load(open('model.pkl','rb'))
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
        locality_lable=float(request.form['locality_lable'])
        type=float(request.form['type'])
        latitude=float(request.form['latitude'])
        longitude=float(request.form['longitude'])
        lease_type=float(request.form['lease_type'])
        gym=float(request.form['gym'])
        lift=float(request.form['lift'])
        swimming_pool=float(request.form['swimming_pool'])
        parking=float(request.form['parking'])
        property_size=float(request.form['property_size'])
        bathroom=float(request.form['bathroom'])
        facing=float(request.form['facing'])
        water_supply=float(request.form['water_supply'])
        balconies=float(request.form['balconies'])
        LIFT=float(request.form['LIFT'])
        INTERNET=float(request.form['INTERNET'])
        AC=float(request.form['AC'])
        INTERCOM=float(request.form['INTERCOM'])
        POOL=float(request.form['POOL'])
        FS=float(request.form['FS'])
        SECURITY=float(request.form['SECURITY'])
        SC=float(request.form['SC'])
        PARK=float(request.form['PARK'])
        HK=float(request.form['HK'])
        PB=float(request.form['PB'])

        prediction = pmodel.predict([locality_lable,type,latitude, longitude , lease_type,gym , lift , swimming_pool , parking, property_size,bathroom , facing , water_supply , balconies,LIFT,INTERNET,AC,INTERCOM,POOL,FS,SECURITY,SC,PARK,HK,PB])
         
        return redirect(url_for('show',score=prediction))

if __name__ == '__main__':
    app.run(debug=True)
