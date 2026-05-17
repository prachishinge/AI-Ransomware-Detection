from flask import Flask, request, jsonify
import pandas as pd
import joblib

# Load model
model = joblib.load("elite_ransomware_model.pkl")

# Load scaler
scaler = joblib.load("scaler.pkl")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])

def predict():

    data = request.json

    df = pd.DataFrame([data])

    scaled_data = scaler.transform(df)

    prediction = model.predict(scaled_data)

    result = int(prediction[0])

    if result == 0:
        label = "Ransomware Detected"
    else:
        label = "Normal Activity"

    return jsonify({
        "prediction": label
    })

if __name__ == "__main__":
    app.run(debug=True)