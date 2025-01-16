import streamlit as st
import numpy as np
from streamlit_extras.let_it_rain import rain
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from scipy.optimize import minimize
import requests
import json
import base64

# To add a local image to Streamlit website
def get_image_base64(image_path):
    """Encodes an image file to a base64 string for HTML rendering."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Path to your local logo image
logo_path = "./ai_farmer_logo_edited.jpg"
logo_base64 = get_image_base64(logo_path)


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


data = pd.read_csv("choy_sum_dataset.csv")

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Separate the independent variables (X) and dependent variable (y)
X = df.drop(columns=["Yield (g/m²)"])
y = df["Yield (g/m²)"]

# Train a multiple linear regression model
multi_linear_regression_model = LinearRegression()
multi_linear_regression_model.fit(X, y)

# Define the negative of the regression model's prediction (we minimize it to maximize yield)
def objective_function(variables):
    # variables = [Temperature, Humidity, Light Intensity, Water pH, etc.]
    input_data = pd.DataFrame([variables], columns=X.columns)
    return -multi_linear_regression_model.predict(input_data)[0]

# Define bounds for each variable
bounds = [
    (15, 30),  # Temperature range
    (40, 80),  # Humidity range
    (10000, 60000),  # Light Intensity range
    (5.5, 7.0),  # Water pH range
    (1.0, 2.5),  # Electrical Conductivity range
    (100, 300),  # Nitrogen Concentration range
    (50, 300),  # Plant Biomass range
    (10, 50)    # Root Volume range
]

# Perform optimization
result = minimize(objective_function, x0=[20, 60, 40000, 6.0, 1.5, 200, 100, 20], bounds=bounds)


# Optimal conditions
optimal_conditions = result.x
print("Optimal Conditions:", optimal_conditions)

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

app_mode = st.sidebar.selectbox("Select page",["CONTEXT","PREDICTIONS", "Pertanian Forum", "PetaniAI"])

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
    test_image = st.file_uploader("Choose an Image:")
    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)

    if(st.button("Predict")):
        print('hi')

elif(app_mode=="Pertanian Forum"):
    # Title of the Forum
    st.title("Pertanian Forum")

    # Initialize session state to store forum posts
    if "forum_posts" not in st.session_state:
        st.session_state.forum_posts = []

    # Popover widget for posting a question
    with st.popover("Post a Question"):  # Using expander as Streamlit doesn't have `st.popover`
        post_username = st.text_input("Your Name", key="post_name")
        post_message = st.text_area("Your Question", key="post_message")
        post_submit = st.button("Post", key="post_submit")

    # Popover widget for answering a question
    with st.popover("Answer a Question"):  # Using expander for dropdown behavior
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
        if post_username.strip() and post_message.strip():
            st.session_state.forum_posts.append({"user": post_username, "question": post_message, "answers": []})
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
    if st.session_state.forum_posts:
        for post in reversed(st.session_state.forum_posts):
            with st.expander(f"**{post['question']}** • From: {post['user']}"):
                for i in st.session_state.forum_posts:
                    st.write(f'{post['answers']} ({post[answer_username]}))
    else:
        st.info("No posts yet. Be the first to post a message!")

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
                <div style="text-align: right;">
                    <strong>You:</strong> {msg["content"]}
                </div>
                """,
                unsafe_allow_html=True,
            )
        elif msg["role"] == "assistant":
            # Left-aligned AI messages with a logo
            st.markdown(
                f"""
                <div style="display: flex; align-items: center; text-align: left;">
                    <img src="data:image/png;base64,{logo_base64}" alt="logo" style="width: 40px; height: 40px; margin-right: 10px;">
                    <div>
                        <strong></strong> {msg["content"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.write('---')


    # # Convert the data into a DataFrame
    # df = pd.DataFrame(data)

    # # Separate the independent variables (X) and dependent variable (y)
    # X = df.drop(columns=["Yield (g/m²)"])
    # y = df["Yield (g/m²)"]

    # # Train a multiple linear regression model
    # multi_linear_regression_model = LinearRegression()
    # multi_linear_regression_model.fit(X, y)

    # # Predict the values
    # y_pred = multi_linear_regression_model.predict()

    # # Print the coefficients and performance metrics
    # print("Coefficients:", multi_linear_regression_model.coef_)
    # print("Intercept:", multi_linear_regression_model.intercept_)
    # print("Mean Squared Error (MSE):", mean_squared_error(y, y_pred))
    # print("R² Score:", r2_score(y, y_pred))

    # # Optional: Display predictions alongside actual values
    # df["Predicted Yield"] = y_pred
    # print("\nData with Predicted Yields:\n", df)
