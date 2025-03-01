# This code builds a Flask-based Weather Forecasting API
#   that allows users to input a year and month and get
#   a predicted temperature using a trained
#   Random Forest Regressor model.'

# Users can query future temperatures through an easy-to-use web API.

import pandas as pd
import numpy as np
from flask import Flask, request, jsonify

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# from sklearn.metrics import mean_squared_error


# Load data
data = pd.read_csv('weather_data.csv')
data = data.dropna(subset=['LandAverageTemperature'])  # Remove NaN values
data['dt'] = pd.to_datetime(data['dt'])
data['year'] = data['dt'].dt.year  # Extract features
data['month'] = data['dt'].dt.month

# Prepare data
features = ['year', 'month']
X = data[features]
y = data['LandAverageTemperature']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=42)

# Train Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


def predict_weather(year, month):
    try:
        year = int(year)
        month = int(month)
    except ValueError:
        raise ValueError("Year and month must be integers.")

    if year < 1970 or year > 2030:
        raise ValueError("Year must be between 1070 and 2030.")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")

    prediction = model.predict([[year, month]])[0]
    return round(prediction, 2)


# Create Flask API
app = Flask(__name__)


@app.route('/predict', methods=['GET'])
def predict():
    try:
        year = request.args.get('year')
        month = request.args.get('month')
        result = predict_weather(year, month)

        return jsonify({"year": year, "month": month, "predicted_temperature": result})

    except ValueError as ve:
        return jsonify({"error": str(ve)})
    except Exception:
        return jsonify({"error": "Invalid input. Please provide valid year and month."})


if __name__ == '__main__':
    app.run(debug=True)
