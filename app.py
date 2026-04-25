import streamlit as st
import pickle
import numpy as np
import os

# 1. Page Configuration
st.set_page_config(page_title="Forest Predictor", page_icon="🌲", layout="centered")

# 2. Load the NEW Random Forest Model
@st.cache_resource
def load_assets():
    model_file = 'forest_model_final.pkl'
    try:
        if os.path.exists(model_file):
            with open(model_file, 'rb') as f:
                model = pickle.load(f)
            return model
        else:
            st.error(f"❌ File '{model_file}' not found in the project folder!")
            return None
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

model = load_assets()

# 3. App Header
st.title("🌲 Forest Cover Type Predictor")
st.markdown("---")

def user_input_features():
    st.sidebar.header("📍 Basic Location Info")
    
    # 10 Numerical features in correct training order
    elevation = st.sidebar.number_input("Elevation (meters)", 1800, 4000, 2500)
    aspect = st.sidebar.slider("Aspect (degrees)", 0, 360, 180)
    slope = st.sidebar.slider("Slope (degrees)", 0, 60, 15)
    hydro_h = st.sidebar.number_input("Horiz. Distance to Water", 0, 1500, 200)
    hydro_v = st.sidebar.number_input("Vert. Distance to Water", -200, 800, 50)
    roadways = st.sidebar.number_input("Distance to Roadways", 0, 8000, 2000)
    
    # Shadow patterns (required to reach 10 numerical features)
    shade_9am, shade_12pm, shade_3pm = 200, 200, 200
    fire_points = st.sidebar.number_input("Distance to Fire Points", 0, 8000, 2000)
    
    # Area selection
    st.sidebar.subheader("Area Environment")
    wilderness_choice = st.sidebar.selectbox(
        "Select Wilderness Area",
        options=["Rawah", "Neota", "Comanche Peak", "Cache la Poudre"]
    )

    # Building the 54-feature vector
    features = [
        elevation, aspect, slope, hydro_h, hydro_v, 
        roadways, shade_9am, shade_12pm, shade_3pm, fire_points
    ]
    
    # Wilderness One-Hot (4 columns)
    wilderness_mapping = {"Rawah": 0, "Neota": 1, "Comanche Peak": 2, "Cache la Poudre": 3}
    wilderness_vector = [0, 0, 0, 0]
    wilderness_vector[wilderness_mapping[wilderness_choice]] = 1
    features.extend(wilderness_vector)
    
    # Soil Types (40 columns) - filled with zeros
    features.extend([0] * 40)
    
    return np.array(features).reshape(1, -1), wilderness_choice

# Execute if model is ready
if model:
    input_df, selected_area = user_input_features()

    # 4. Prediction Logic
    st.write("### Analysis Results")
    if st.button("Predict Tree Species ✨"):
        # Direct prediction from Random Forest
        prediction = model.predict(input_df)
        
        tree_types = {
            1: "Spruce/Fir",
            2: "Lodgepole Pine",
            3: "Ponderosa Pine",
            4: "Cottonwood/Willow",
            5: "Aspen",
            6: "Douglas-fir",
            7: "Krummholz"
        }
        
        result = tree_types.get(prediction[0], "Unknown")
        
        # UI Display
        st.success(f"## Predicted Species: **{result}**")
        st.balloons()
        
        st.info(f"Model analysis for **{selected_area}** at **{input_df[0][0]}m** elevation.")
else:
    st.warning("⚠️ Please ensure 'forest_model_final.pkl' is in the project folder.")