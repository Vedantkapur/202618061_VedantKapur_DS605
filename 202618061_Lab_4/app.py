import streamlit as st
import pandas as pd
import joblib

# Page Configuration

st.set_page_config(
    page_title="NYC Airbnb Price Predictor",
    layout="centered"
)

# Loading Model

@st.cache_resource
def load_model():
    return joblib.load("airbnb_price_pipeline.pkl")


model = load_model()

# Application Title

st.title("NYC Airbnb Price Predictor")

st.write(
    """
    Enter the details of an Airbnb listing to estimate
    its expected nightly price in New York City.
    """
)

# User Inputs

neighbourhood_group = st.selectbox(
    "Neighbourhood Group",
    [
        "Manhattan",
        "Brooklyn",
        "Queens",
        "Bronx",
        "Staten Island"
    ]
)


neighbourhood = st.text_input(
    "Neighbourhood",
    value="Midtown"
)


room_type = st.selectbox(
    "Room Type",
    [
        "Entire home/apt",
        "Private room",
        "Shared room"
    ]
)


latitude = st.number_input(
    "Latitude",
    min_value=40.4,
    max_value=40.95,
    value=40.75,
    format="%.6f"
)


longitude = st.number_input(
    "Longitude",
    min_value=-74.3,
    max_value=-73.6,
    value=-73.98,
    format="%.6f"
)


host_id = st.number_input(
    "Host ID",
    min_value=0,
    value=100000,
    step=1
)


minimum_nights = st.number_input(
    "Minimum Nights",
    min_value=1,
    max_value=365,
    value=2,
    step=1
)


number_of_reviews = st.number_input(
    "Number of Reviews",
    min_value=0,
    value=25,
    step=1
)


reviews_per_month = st.number_input(
    "Reviews per Month",
    min_value=0.0,
    value=1.5,
    step=0.1
)


calculated_host_listings_count = st.number_input(
    "Host Listings Count",
    min_value=1,
    value=1,
    step=1
)


availability_365 = st.number_input(
    "Availability (Days per Year)",
    min_value=0,
    max_value=365,
    value=250,
    step=1
)


has_reviews = 1 if number_of_reviews > 0 else 0

# Prediction

if st.button("💰 Predict Price"):

    input_data = pd.DataFrame({
        "host_id": [host_id],
        "neighbourhood_group": [neighbourhood_group],
        "neighbourhood": [neighbourhood],
        "latitude": [latitude],
        "longitude": [longitude],
        "room_type": [room_type],
        "minimum_nights": [minimum_nights],
        "number_of_reviews": [number_of_reviews],
        "reviews_per_month": [reviews_per_month],
        "calculated_host_listings_count": [
            calculated_host_listings_count
        ],
        "availability_365": [availability_365],
        "has_reviews": [has_reviews]
    })


    prediction = model.predict(input_data)[0]


    st.success(
        f"Estimated Nightly Price: ${prediction:.2f}"
    )