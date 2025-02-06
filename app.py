from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
model = load(open("/workspaces/ml-webapp-using-flask-tutorial-pn/Breast_Cancer_Classifier.pkl", "rb"))
class_dict = {
    "0": "Remission",
    "1": "Non-remission"
}

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        val1 = int(request.form["val1"])
        val2 = int(request.form["val2"])
        val3 = int(request.form["val3"])
        val4 = 0
        val5 = 0
        val6 = int(request.form["val6"])
        val7 = int(request.form["val7"])
        val8 = int(request.form["val8"])
        val9 = int(request.form["val9"])
        
        data = [[val1, val2, val3, val4, val5, val6, val7, val8, val9]]
        prediction = str(model.predict(data)[0])
        pred_class = class_dict[prediction]
    else:
        pred_class = None
    
    return render_template("index.html", prediction = pred_class)