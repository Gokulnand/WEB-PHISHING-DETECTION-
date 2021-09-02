from flask import Flask, render_template, request

import FeatureExtraction
import pickle

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/getURL',methods=['GET','POST'])
def getURL():
    if request.method == 'POST':
        url = request.form['url']
        #print(url)
        data = FeatureExtraction.getAttributess(url)
        #print(data)
        RFmodel = pickle.load(open('RandomForestModel.sav', 'rb'))
        predicted_value = RFmodel.predict(data)
        #print(predicted_value)
        if predicted_value == 0:    
            value = 0
            return render_template("home.html",error=value)
        else:
            value = 1
            return render_template("home.html",error=value)
if __name__ == "__main__":
    app.run(debug=True)
