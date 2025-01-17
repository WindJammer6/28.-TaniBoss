import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from streamlit_extras.let_it_rain import rain
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split  
from sklearn.metrics import mean_squared_error, r2_score
from scipy.optimize import minimize
import requests
import json
import base64
from datetime import datetime

########################
# Administrative codes #
########################
st.set_page_config(page_title='Snowflake', layout='wide',
                #    initial_sidebar_state=st.session_state.get('sidebar_state', 'collapsed'),
)
sidebar_content = """
<div style="display: flex; justify-content: center; align-items: center;">
    <img src="https://toagriculture.com/wp-content/uploads/2022/09/Plant-diseases.jpg" width="1000">
</div>
"""

st.markdown(sidebar_content, unsafe_allow_html=True)

cols = st.columns(2)


# //////////////////////////////////////////////////////////////////////


# Preparing the dataset, and training a Multiple Linear Regression model with the dataset
# Load the dataset
file_path = "crop_yield_dataset.csv"
data = pd.read_csv(file_path)

# Calculate the average yield for the crop
avg_yield = data['Yield (Q/acre)'].mean()
    
# Filter rows with yield above the average
filtered_data = data[data['Yield (Q/acre)'] > avg_yield].head(250)

# Define features (X) and target (y)
X = filtered_data[['Rain Fall (mm)', 'Nitrogen (N)', 
                    'Phosphorus (P)', 'Potassium (K)']]  # Features
# X = filtered_data[['Rain Fall (mm)', 'Temperature', 'Nitrogen (N)', 
#                     'Phosphorus (P)', 'Potassium (K)']]  # Features
y = filtered_data['Yield (Q/acre)']  # Target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print results
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2): {r2:.2f}")

# Display coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)


# //////////////////////////////////////////////////////////////////////


# Define function to separate into quartiles and provide recommendations
def analyze_and_recommend(data, farmer_input):
    
    all_optimal = True
    # Sort data by yield and select the upper half for training
    # upper_half = data[data["Yield (Q/acre)"] >= data["Yield (Q/acre)"].median()]
    
    # Compute quartile ranges for the upper half
    quartiles = pd.qcut(data["Yield (Q/acre)"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])
    data["Quartile"] = quartiles
    
    # Select the highest quartile (Q4: 75%–100% yield)
    highest_quartile = data[data["Quartile"] == "Q4"]
    
    # Compute mean yield and feature values for the highest quartile
    mean_values = highest_quartile.mean(numeric_only=True)
    mean_yield = mean_values["Yield (Q/acre)"]
    
    # Compare farmer's input to mean values and generate recommendations
    recommendations = {}
    for feature in farmer_input.keys():
        farmer_value = farmer_input[feature]
        ideal_value = mean_values[feature]
        if farmer_value < ideal_value - 0.05 * ideal_value:
            all_optimal = False
            recommendations[feature] = f":arrow_up_small: :green[Increase] {feature} to around {ideal_value:.2f}."
        elif farmer_value > ideal_value + 0.05 * ideal_value:
            all_optimal = False
            recommendations[feature] = f":arrow_up_small: :red[Decrease] {feature} to around {ideal_value:.2f}."
        else:
            recommendations[feature] = f"{feature} is optimal."
    
    return mean_yield, mean_values, recommendations, all_optimal


# To add a local image to Streamlit website
def get_image_base64(image_path):
    """Encodes an image file to a base64 string for HTML rendering."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Path to your local logo image
logo_path_user = "./user_logo.jpg"
logo_path_farmer_ai = "./ai_farmer_logo_edited.jpg"
logo_path_site_analysis = "./siteanalysis_hydroponic.jpg"
logo_base64_user = get_image_base64(logo_path_user)
logo_base64_farmer_ai = get_image_base64(logo_path_farmer_ai)
logo_base64_site_analysis = get_image_base64(logo_path_site_analysis)

# Rain effect
def rain_emojis_of_water():
    rain(
        emoji="💧",
        font_size=40,
        falling_speed=1,
        animation_length=1000,
    )
rain_emojis_of_water()

# Initiating Chatbase stuffs
url = 'https://www.chatbase.co/api/v1/chat'
headers = {
    'Authorization': 'Bearer 3c7b798b-c5fe-41a7-bdeb-f5d0b6f8536e',
    'Content-Type': 'application/json'
}
# Initialize conversation history in session state
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = {
        "messages": [],
        "chatbotId": "wGS8ehg-39TolweihWY3w",
        "stream": False,
        "temperature": 0
    }


#################
# Sidebar codes #
#################
st.sidebar.title("FarmsOnly🌱💧")
st.sidebar.caption("Made by Group 5: [Joshua](https://www.instagram.com/joshuaoliveryoung?igsh=dHpsanVveHIxZDVy&utm_source=qr), [Shelly](https://www.linkedin.com/in/ShellyWijayaOei/), [Kelly](https://www.linkedin.com/in/kelly-patricia-233a63241?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app), [Chua Xing Han](https://linktr.ee/cxinghan), [Cheah Hoe Teng](https://www.linkedin.com/in/hoe-teng-cheah-938111275/) and [Goh Jet Wei](https://www.linkedin.com/in/gohjetwei)")
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

app_mode = st.sidebar.selectbox("Select page",["Context","Predictor", "Pertanian Forum", "PetaniAI"])

st.sidebar.caption("")
st.sidebar.caption("")
st.sidebar.caption("")

st.sidebar.success("""
                **What does FarmsOnly do?**  
                FarmsOnly is targeted at local farmers in Gunung Anyar, Surabaya, Indonesia, to help them make better decisions in their hydroponic farming to optimise crop yield.
                FarmsOnly provides a multitude of features including:
                - **Our flagship prediction and recommendation machine learning model**
                - **Pertanian forum**
                - **PertaniAI**
                   
                to help local farmers improve their crop yield based on their current farming practices
"""
)

with st.sidebar.expander("Acknowledgments"):
    st.markdown("""
    We are incredibly grateful to the locals at Gunung Anyar, Surabaya, Indonesia, who were willing to bring us around their hydroponic farm and inspiring us to come up with this project idea. 
    """)



######################
# Context page codes #
######################
if(app_mode=="Context"):
    st.markdown("<h1 style='text-align: center;'>Why FarmsOnly?", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center;">
            <img src="data:image/png;base64,{logo_base64_site_analysis}" alt="logo" style="width: 40%;">
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write('')
    st.write("""After our visit to Edufarm, Gunung Anyar, we found that the farmers were facing a critical issue regarding their hydroponic farming 
             techniques. Certain crops such as choy sum, kang kong have not been yielding well, causing them much pain and frustration. Despite 
             making attempts to improve the conditions and trying suggestions found on the internet, they are still unable to solve the problem, 
             causing their crops to die prematurely, affecting yield.""")
             
    st.write("""Hence, we present **FarmsOnly**, an innovative solution that utilises machine learning techniques to generate suggestions for optimising 
             hydroponic techniques, based on the conditions and yield at Gunung Anyar. Additionally, it offers a platform for farmers to communicate with one another, 
             allowing them to ask for and share advice on localised farming techniques. Lastly, it offers an expert hydroponic farming AI assistant to 
             provide secondary advice to their current hydroponic farming techniques.""")

########################
# Predictor page codes #
########################
elif(app_mode=="Predictor"):
    st.markdown("<h1 style='text-align: center;'>Predictor and Recommendation Model 🧠🤖", unsafe_allow_html=True)
    st.header("Train the Model 🏋️")
    st.caption("You can enter today's conditions of the farm to further train the model to improve its prediction accuracy!")
    side_left_col_train, side_right_col_train = st.columns(2)
    rainfall_train = side_left_col_train.text_input('Rainfall (ppm):')
    # temperature_train = side_left_col_train.text_input('Temperature (in °C):')
    nitrogen_train = side_left_col_train.text_input('Nitrogen (g):')
    phosphorus_train = side_right_col_train.text_input('Phosphorus (g):')
    potassium_train = side_right_col_train.text_input('Potassium (g):')
    yield_train = side_left_col_train.text_input('Yield (g/m²):')

    if side_left_col_train.button('Submit'):
        st.success("Today's condition the farm has been received by the model!")

    st.write("---")
    st.header("Predict with Model 📋")
    st.caption("You can enter today's conditions of the farm to further train the model to improve its prediction accuracy!")
    side_left_col_predict, side_right_col_predict = st.columns(2)
    rainfall_predict = side_left_col_predict.text_input('Rainfall (ppm):', key=100)
    # temperature_predict = side_left_col_predict.text_input('Temperature (in °C):', key=200)
    nitrogen_predict = side_left_col_predict.text_input('Nitrogen (g):', key=300)
    phosphorus_predict = side_right_col_predict.text_input('Phosphorus (g):', key=400)
    potassium_predict = side_right_col_predict.text_input('Potassium (g):', key=500)

    if(st.button("Predict")):      
        st.success("Success!")

        farmer_input_conditions = {
            'Rain Fall (mm)': int(rainfall_predict),
            # 'Temperature': int(temperature_predict),
            'Nitrogen (N)': int(nitrogen_predict),
            'Phosphorus (P)': int(phosphorus_predict),
            'Potassium (K)': int(potassium_predict)
        }

        # Analyze data and provide recommendations
        mean_yield, mean_values, recommendations, all_optimal = analyze_and_recommend(data, farmer_input_conditions)

        # Display results
        st.write(f"Mean Yield for the highest quartile of crop: {mean_yield:.2f}")
        # st.write("\nFeature values for the mean yield of the highest quartile:")
        # st.write(mean_values)
        df = pd.DataFrame(index=["Average", "Current"])
        for condition in farmer_input_conditions.items():
            col = condition[0]
            df[col] = [mean_values[col], condition[1]]
        cols = st.columns(df.shape[1])
 
        # Sample data for the bar charts
        data1 = df["Rain Fall (mm)"]
        data2 = df["Nitrogen (N)"]
        data3 = df["Phosphorus (P)"]
        data4 = df["Potassium (K)"]

        # Create a 4x1 grid using st.columns
        col1, col2, col3, col4 = st.columns(4)

        # Display each chart in its respective column
        with col1:
            st.subheader("Rain Fall (mm)")
            st.bar_chart(data1)

        with col2:
            st.subheader("Nitrogen (N)")
            st.bar_chart(data2)

        with col3:
            st.subheader("Phosphorus (P)")
            st.bar_chart(data3)

        with col4:
            st.subheader("Potassium (K)")
            st.bar_chart(data4)

        if all_optimal:
            st.write("No further action necessary. Your farm is already optimized for high yield!")
        else:
            st.write("\nRecommendations for improving yield:")
        for feature, recommendation in recommendations.items():
            st.write(f"- {recommendation}")

##############################
# Pertanian forum page codes #
##############################
elif(app_mode=="Pertanian Forum"):
    # Title of the Forum
    st.title("Pertanian Forum 🗣️")

    # Initialize session state to store forum posts
    if "forum_posts" not in st.session_state:
        st.session_state.forum_posts = []

    # Popover widget for posting a question
    with st.popover("Post a Question!"):  # Using expander as Streamlit doesn't have `st.popover`
        post_username = st.text_input("Your Name", key="post_name")
        post_message = st.text_area("Your Question", key="post_message")
        post_submit = st.button("Post", key="post_submit")

    # Popover widget for answering a question
    with st.popover("Answer a Question!"):  # Using expander for dropdown behavior
        answer_username = st.text_input("Your Name", key="answer_name")
        temp_list = []
        for i in range(len(st.session_state.forum_posts)):
            if st.session_state.forum_posts:
                temp_list.append(st.session_state.forum_posts[i]['question']) 
        question_to_answer = st.selectbox('Question to Answer', temp_list)
        answer_message = st.text_area("Your Answer", key="answer_message")
        answer_submit = st.button("Post", key="answer_submit")

    # Handle posting a question
    if post_submit:
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M")

        if post_username.strip() and post_message.strip():
            st.session_state.forum_posts.append({"user": post_username, "question": post_message, "answers": [], 'datetime': formatted_datetime})
            st.success("Question posted successfully!")
        else:
            st.error("Please fill in both fields.")

    # Handle posting an answer
    if answer_submit:
        if answer_username.strip() and answer_message.strip() and question_to_answer.strip():
            for i in st.session_state.forum_posts:
                if i['question'] == question_to_answer:
                    i['answers'].append(answer_message)
            st.success("Answer posted successfully!")
        else:
            st.error("Please fill in all fields.")

    # Display forum messages
    st.write('---')
    st.header('Posts')

    if st.session_state.forum_posts:
        for post in reversed(st.session_state.forum_posts):
            with st.expander(f"**{post['question']}** • From: {post['user']} • On: {post['datetime']}"):
                st.write('Responses:')
                for i in range(len(post['answers'])):
                    temp_answer_posts = post['answers'][i]
                    st.write(f'- {temp_answer_posts} (From: {answer_username})')
    else:
        st.info("No posts yet. Be the first to post a message!")

########################
# PertaniAI page codes #
########################
elif app_mode == "PetaniAI":
    # Streamlit app setup
    st.title("PetaniAI")
    st.subheader("Ask me anything!")

    # Input box for user query
    user_input = st.text_input("Your message:")

    # Submit button
    if st.button("Send"):
        if user_input.strip():
            # Append the user message to session state
            st.session_state.conversation_history["messages"].append({"content": user_input, "role": "user"})

            # Generate response using the Chatbase API
            response = requests.post(
                url, 
                headers=headers, 
                data=json.dumps(st.session_state.conversation_history)
            )
            json_data = response.json()

            # Handle response
            if response.status_code == 200:
                # Append the AI response to session state
                st.session_state.conversation_history["messages"].append(
                    {"content": json_data['text'], "role": "assistant"}
                )
            else:
                st.error(f"Error: {json_data.get('message', 'Unknown error')}. Please try again.")

    # Display the conversation history
    for msg in st.session_state.conversation_history["messages"]:
        if msg["role"] == "user":
            # Right-aligned user messages
            st.markdown(
                f"""
                <div style="display: flex; justify-content: flex-end; align-items: center; text-align: right;">
                    <div style="margin-right: 10px;">
                        {msg["content"]}
                    </div>
                    <img src="data:image/png;base64,{logo_base64_user}" alt="logo" style="width: 40px; height: 40px;">
                </div>
                """,
                unsafe_allow_html=True,
            )
        elif msg["role"] == "assistant":
            # Left-aligned AI messages with a logo
            st.markdown(
                f"""
                <div style="display: flex; align-items: center; text-align: left;">
                    <img src="data:image/png;base64,{logo_base64_farmer_ai}" alt="logo" style="width: 40px; height: 40px; margin-right: 10px;">
                    <div>
                        <strong></strong> {msg["content"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.write('---')
