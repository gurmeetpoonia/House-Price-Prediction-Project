
import streamlit as st
import joblib
import numpy as np 
import pandas as pd
model = joblib.load("house_price_model.pkl")
st.title("🏠 House Price Prediction")
#inputs 
area = st.number_input("Area (sq ft)", min_value=0, step=1)
bedrooms = st.number_input("Bedrooms", min_value=0, step=1)
bathrooms = st.number_input("Bathrooms", min_value=0, step=1)
stories = st.number_input("Stories", min_value=0, step=1)
parking = st.number_input("Parking", min_value=0, step=1)
mainroad=st.selectbox("Mainroad",["Select", "Yes","No"])
guestroom=st.selectbox("Guestroom",["Select", "Yes","No"])
basement=st.selectbox("Basement",["Select", "Yes","No"])
hotwaterheating=st.selectbox("Hot water heating",["Select", "Yes","No"])
airconditioning=st.selectbox("Air conditioning",["Select", "Yes","No"])
prefarea=st.selectbox("Prefarea",["Select", "Yes","No"])
furnishingstatus=st.selectbox("Furnishingstatus",["Select", "Unfurnished","Semi-Furnished","Furnished"])

#encoding 



if st.button("Predict"):

    if area <= 0:
        st.warning("Please enter Area")

    elif bedrooms <= 0:
        st.warning("Please enter Bedrooms")

    elif bathrooms <= 0:
        st.warning("Please enter Bathrooms")

    elif (
        mainroad == "Select" or
        guestroom == "Select" or
        basement == "Select" or
        hotwaterheating == "Select" or
        airconditioning == "Select" or
        prefarea == "Select" or
        furnishingstatus == "Select"
    ):
        st.warning("Please fill all dropdown fields")

    else:
        # encoding
        mainroad = 1 if mainroad == "Yes" else 0
        guestroom = 1 if guestroom == "Yes" else 0
        basement = 1 if basement == "Yes" else 0
        hotwaterheating = 1 if hotwaterheating == "Yes" else 0
        airconditioning = 1 if airconditioning == "Yes" else 0
        prefarea = 1 if prefarea == "Yes" else 0

        furnishingstatus = {
            "Unfurnished": 0,
            "Semi-Furnished": 1,
            "Furnished": 2
        }[furnishingstatus]

        # prediction

        input_data = pd.DataFrame(
            [[
                area,
                bedrooms,
                bathrooms,
                stories,
                parking,
                mainroad,
                guestroom,
                basement,
                hotwaterheating,
                airconditioning,
                prefarea,
                furnishingstatus
            ]],
            columns=[
                "area",
                "bedrooms",
                "bathrooms",
                "stories",
                "parking",
                "mainroad",
                "guestroom",
                "basement",
                "hotwaterheating",
                "airconditioning",
                "prefarea",
                "furnishingstatus"
            ]
        )
        
        prediction = model.predict(input_data)

import streamlit as st
import joblib
import numpy as np 
import pandas as pd
model = joblib.load("house_price_model.pkl")
st.title("🏠 House Price Prediction")
#inputs 
area = st.number_input("Area (sq ft)", min_value=0, step=1)
bedrooms = st.number_input("Bedrooms", min_value=0, step=1)
bathrooms = st.number_input("Bathrooms", min_value=0, step=1)
stories = st.number_input("Stories", min_value=0, step=1)
parking = st.number_input("Parking", min_value=0, step=1)
mainroad=st.selectbox("Mainroad",["Select", "Yes","No"])
guestroom=st.selectbox("Guestroom",["Select", "Yes","No"])
basement=st.selectbox("Basement",["Select", "Yes","No"])
hotwaterheating=st.selectbox("Hot water heating",["Select", "Yes","No"])
airconditioning=st.selectbox("Air conditioning",["Select", "Yes","No"])
prefarea=st.selectbox("Prefarea",["Select", "Yes","No"])
furnishingstatus=st.selectbox("Furnishingstatus",["Select", "Unfurnished","Semi-Furnished","Furnished"])

#encoding 



if st.button("Predict"):

    if area <= 0:
        st.warning("Please enter Area")

    elif bedrooms <= 0:
        st.warning("Please enter Bedrooms")

    elif bathrooms <= 0:
        st.warning("Please enter Bathrooms")

    elif (
        mainroad == "Select" or
        guestroom == "Select" or
        basement == "Select" or
        hotwaterheating == "Select" or
        airconditioning == "Select" or
        prefarea == "Select" or
        furnishingstatus == "Select"
    ):
        st.warning("Please fill all dropdown fields")

    else:
        # encoding
        mainroad = 1 if mainroad == "Yes" else 0
        guestroom = 1 if guestroom == "Yes" else 0
        basement = 1 if basement == "Yes" else 0
        hotwaterheating = 1 if hotwaterheating == "Yes" else 0
        airconditioning = 1 if airconditioning == "Yes" else 0
        prefarea = 1 if prefarea == "Yes" else 0

        furnishingstatus = {
            "Unfurnished": 0,
            "Semi-Furnished": 1,
            "Furnished": 2
        }[furnishingstatus]

        # prediction

        input_data = pd.DataFrame(
            [[
                area,
                bedrooms,
                bathrooms,
                stories,
                parking,
                mainroad,
                guestroom,
                basement,
                hotwaterheating,
                airconditioning,
                prefarea,
                furnishingstatus
            ]],
            columns=[
                "area",
                "bedrooms",
                "bathrooms",
                "stories",
                "parking",
                "mainroad",
                "guestroom",
                "basement",
                "hotwaterheating",
                "airconditioning",
                "prefarea",
                "furnishingstatus"
            ]
        )
        
        prediction = model.predict(input_data)
        st.success(f"🏠 Estimated House Price: ₹{prediction[0]:,.0f}")