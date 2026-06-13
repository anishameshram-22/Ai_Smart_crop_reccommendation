import numpy as np
import pandas as pd
import pickle

# Load the trained Random Forest Classifier model
with open('model.pkl', 'rb') as model_file:
    rfc = pickle.load(model_file)

# Load the fitted StandardScaler
with open('scaler.pkl', 'rb') as scaler_file:
    sc = pickle.load(scaler_file)

# Define the crop dictionary (assuming it's constant for prediction)
crop_dict = {
    'apple': 0, 'banana': 1, 'blackgram': 2, 'chickpea': 3, 'coconut': 4, 'coffee': 5,
    'cotton': 6, 'grapes': 7, 'jute': 8, 'kidneybeans': 9, 'lentil': 10, 'maize': 11,
    'mango': 12, 'mothbeans': 13, 'mungbean': 14, 'muskmelon': 15, 'orange': 16,
    'papaya': 17, 'pigeonpeas': 18, 'pomegranate': 19, 'rice': 20, 'watermelon': 21
}

def reccommendaion(N, P, K, temperature, humidity, ph, rainfall):
    # Prepare the input data as a NumPy array
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    # Scale the input data using the loaded StandardScaler
    input_data_scaled = sc.transform(input_data)

    # Make a prediction using the loaded Random Forest Classifier
    prediction_encoded = rfc.predict(input_data_scaled)
    predicted_crop_num = prediction_encoded[0]

    # Reverse lookup the crop name from crop_dict
    # Convert crop_dict values to integers for consistent comparison
    predicted_crop_name = [crop for crop, num in crop_dict.items() if num == predicted_crop_num][0]

    return predicted_crop_name

# Example usage in app.py:
if __name__ == "__main__":
    # Example input values
    N = 20
    P = 30
    K = 40
    temperature = 40.0
    humidity = 20
    ph = 30
    rainfall = 50

    # Get the recommendation
    recommended_crop = reccommendaion(N, P, K, temperature, humidity, ph, rainfall)
    print(f"Based on the given conditions, the recommended crop is: {recommended_crop}")
