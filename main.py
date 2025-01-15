import streamlit as st
import numpy as np
from streamlit_extras.let_it_rain import rain
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) 
    predictions = model.predict(input_arr)
    return np.argmax(predictions) 

def rain_emojis_of_water():
    rain(
        emoji="💧",
        font_size=40,
        falling_speed=1,
        animation_length=1000,
    )

st.set_page_config(page_title='Snowflake', layout='wide',
                #    initial_sidebar_state=st.session_state.get('sidebar_state', 'collapsed'),
)
sidebar_content = """
<div style="display: flex; justify-content: center; align-items: center;">
    <img src="https://toagriculture.com/wp-content/uploads/2022/09/Plant-diseases.jpg" width="1000">
</div>
"""

st.markdown(sidebar_content, unsafe_allow_html=True)

rain_emojis_of_water()

cols = st.columns(2)


#################
# Sidebar codes #
#################
st.sidebar.title("Plant Disease Detection System for Sustainable Agriculture for Hydroponic Farming in Gunung Anyar, Surabaya, Indonesia🌱💧")
st.sidebar.caption("Made by Group 5: Joshua, [Shelly](https://www.linkedin.com/in/ShellyWijayaOei/), [Kelly](https://www.linkedin.com/in/kelly-patricia-233a63241?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app), [Chua Xing Han](https://linktr.ee/cxinghan), [Cheah Hoe Teng](https://www.linkedin.com/in/hoe-teng-cheah-938111275/) and [Goh Jet Wei](https://www.linkedin.com/in/gohjetwei)")
st.sidebar.caption("In collboration with:")

sidebar_content = """
<div style="display: flex; align-items: center;">
    <img src="https://serviceomni.petra.ac.id/resources/9ad247aa-98ac-475a-a2b5-d50903a2a128" width="70" style="margin-right: 10px;">
    <span style="font-size: 14px; margin-right: 10px;">|</span>
    <img src="https://cdn.freelogovectors.net/wp-content/uploads/2022/03/sutd_logo_freelogovectors.net_.png" width="150" style="margin-right: 10px;">
</div>
"""

st.sidebar.markdown(sidebar_content, unsafe_allow_html=True)
st.sidebar.caption("")
st.sidebar.caption("")
st.sidebar.caption("")

app_mode = st.sidebar.selectbox("Select between 'CONTEXT' page and 'PREDICTIONS' page",["CONTEXT","PREDICTIONS"])

st.sidebar.caption("")
st.sidebar.caption("")
st.sidebar.caption("")

st.sidebar.success("""
                **What can this Streamlit website do?**  
                Allows us to make predictions on... See more in the 'CONTEXT' page
"""
)

with st.sidebar.expander("Acknowledgments"):
    st.markdown("""
    We are incredibly grateful to the locals at Gunung Anyar, Surabaya, Indonesia, who were willing to bring us around their hydroponic farm and inspiring us to come up with this project idea. 
    """)


##################
# Mainpage codes #
##################
if(app_mode=="CONTEXT"):
    st.markdown("<h1 style='text-align: center;'>Context of the Problem", unsafe_allow_html=True)
    st.write("I found out that they have a little problem with their hydroponic plants. Their spinach sometimes wont grow well. The person taking care of the plants still couldnt figure out the right nutrition for the spinach to grow well all the time. So maybe create a machine learning web to give them recommendation on what to do w/ the plants, considering the weather and other factors lol")
    st.markdown("<h2 style='text-align: center;'>Our Personas 👨‍👨‍👦‍👦", unsafe_allow_html=True)


elif(app_mode=="PREDICTIONS"):
    st.markdown("<h1 style='text-align: center;'>Plant Disease Detection System for Sustainable Agriculture Predictor", unsafe_allow_html=True)
    st.
    test_image = st.file_uploader("Choose an Image:")
    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)
    if(st.button("Predict")):
        st.snow()
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                      'Tomato___healthy']
        st.success("Model is Predicting it's a {}".format(class_name[result_index]))

    data = pd.read_csv("choy_sum_dataset.csv")

    # Convert the data into a DataFrame
    df = pd.DataFrame(data)

    # Separate the independent variables (X) and dependent variable (y)
    X = df.drop(columns=["Yield (g/m²)"])
    y = df["Yield (g/m²)"]

    # Train a multiple linear regression model
    multi_linear_regression_model = LinearRegression()
    multi_linear_regression_model.fit(X, y)

    # Predict the values
    y_pred = multi_linear_regression_model.predict()

    # Print the coefficients and performance metrics
    print("Coefficients:", multi_linear_regression_model.coef_)
    print("Intercept:", multi_linear_regression_model.intercept_)
    print("Mean Squared Error (MSE):", mean_squared_error(y, y_pred))
    print("R² Score:", r2_score(y, y_pred))

    # Optional: Display predictions alongside actual values
    df["Predicted Yield"] = y_pred
    print("\nData with Predicted Yields:\n", df)
