This is a Flask-based web API that predicts future temperatures based on historical weather data using a Random Forest Regressor model. Users can input a year and month to receive a predicted temperature.

# Features:
* Predicts average land temperature for a given year and month.
* Uses machine learning (Random Forest Regressor) for forecasting.
* RESTful API with input validation and error handling.
* Simple and user-friendly interface for querying predictions.

# Technology used:
* Python
* Flask (Web framework for API)
* Scikit-learn (Machine Learning)
* Pandas & NumPy (Data processing)

# Installation & Setup

## Clone the repository:
```
git clone https://github.com/yourusername/weather-forecast-api.git
cd weather-forecast-api
```

## Install dependencies:
```
pip install -r requirements.txt
```

## Run the Flask application:
```
python3 Api.py
```

## Access the API at:
```
http://127.0.0.1:5000/predict?year=2025&month=7
```

# API Usage

Endpoint: ```/predict```
Method: **GET**

Parameters:
1. Year (int) → The year for prediction (1970-2030)
2. Month (int) → The month for prediction (1-12)
   
### Example Request:
```
http://127.0.0.1:5000/predict?year=2025&month=7
```
### Example Response:
```
{
    "year": 2025,
    "month": 7,
    "predicted_temperature": 16.32
}
```

# Contributions
Contributions are welcome! Feel free to submit issues or pull requests.
