from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load saved model
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    hours = float(request.form["hours"])
    attendance = float(request.form["attendance"])

    sample = np.array([[hours, attendance]])

    prediction = model.predict(sample)

    if prediction[0] == 1:
        result = "🎉 Prediction: PASS"
    else:
        result = "❌ Prediction: FAIL"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)