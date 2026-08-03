from flask import Flask
import pickle
import numpy as np

app = Flask(__name__)

# Load saved model
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():

    sample = np.array([[6, 85]])

    prediction = model.predict(sample)

    if prediction[0] == 1:
        return "Prediction: PASS 🎉"

    return "Prediction: FAIL"

if __name__ == "__main__":
    app.run(debug=True)