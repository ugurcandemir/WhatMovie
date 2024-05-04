from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load('models/model.pkl')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get data from the request
#     data = request.json
    
#     # Perform any necessary preprocessing on the data
#     # Example: Convert data to DataFrame and apply preprocessing
    
#     # Make predictions using the loaded model
#     predictions = model.predict(data)
    
#     # Return the predictions
#     return jsonify({'predictions': predictions.tolist()}), 200

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    data = request.json
    
    # Perform any necessary preprocessing on the data
    # Example: Convert data to DataFrame and apply preprocessing
    
    # Extract input features from the data
    input_features = pd.DataFrame(data, index=[0])  # Assuming data is a dictionary
    
    # Make predictions using the loaded model
    predictions = model.predict(input_features)
    
    # Return the predictions
    return jsonify({'predictions': predictions.tolist()}), 200


if __name__ == '__main__':
    app.run(debug=True)
