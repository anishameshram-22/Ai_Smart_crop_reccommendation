import streamlit as st
import pickle
import numpy as np

st.set_page_config(
    page_title="AI Smart Crop Recommendation",
    page_icon="🌱",
    layout="wide"
)

# Load Models
try:
    model = pickle.load(open("model.pkl", "rb"))
    sc = pickle.load(open("standscaler.pkl", "rb"))
    ms = pickle.load(open("minmaxscaler.pkl", "rb"))
except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

st.title("🌱 AI Smart Crop Recommendation System")
st.markdown("Enter soil nutrients and weather conditions to get the best crop recommendation.")

col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", min_value=0.0)
    P = st.number_input("Phosphorus (P)", min_value=0.0)
    K = st.number_input("Potassium (K)", min_value=0.0)
    temp = st.number_input("Temperature (°C)", min_value=0.0)

with col2:
    humidity = st.number_input("Humidity (%)", min_value=0.0)
    ph = st.number_input("Soil pH", min_value=0.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0)

if st.button("Recommend Crop"):
    try:
        feature_list = [N, P, K, temp, humidity, ph, rainfall]

        single_pred = np.array(feature_list).reshape(1, -1)

        scaled_features = ms.transform(single_pred)
        final_features = sc.transform(scaled_features)

        prediction = model.predict(final_features)

        crop_dict = {
            1: "Rice",
            2: "Maize",
            3: "Jute",
            4: "Cotton",
            5: "Coconut",
            6: "Papaya",
            7: "Orange",
            8: "Apple",
            9: "Muskmelon",
            10: "Watermelon",
            11: "Grapes",
            12: "Mango",
            13: "Banana",
            14: "Pomegranate",
            15: "Lentil",
            16: "Blackgram",
            17: "Mungbean",
            18: "Mothbeans",
            19: "Pigeonpeas",
            20: "Kidneybeans",
            21: "Chickpea",
            22: "Coffee"
        }

        crop = crop_dict.get(
            int(prediction[0]),
            "No suitable crop found"
        )

        st.success(f"✅ Recommended Crop: {crop}")

    except Exception as e:
        st.error(f"Prediction Error: {e}")
