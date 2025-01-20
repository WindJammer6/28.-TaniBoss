# 18.-TaniBoss! 
<p align="center"> 
  <img src="https://github.com/WindJammer6/18.-Deployed-Streamlit-Python-and-Firebase-Web-Application-Project-for-a-Karaoke-Event/blob/main/README%20images/Image%20of%20Streamlit%20(Python)%20Karaoke%20Singer%20Registration%20web%20application.jpg"  width="350" height="250">
  <img src="https://github.com/WindJammer6/18.-Deployed-Streamlit-Python-and-Firebase-Web-Application-Project-for-a-Karaoke-Event/blob/main/README%20images/Image%20of%20Streamlit%20(Python)%20Karaoke%20Singer%20Registration%20web%20application.jpg"  width="350" height="250">
  <img src="https://github.com/WindJammer6/18.-Deployed-Streamlit-Python-and-Firebase-Web-Application-Project-for-a-Karaoke-Event/blob/main/README%20images/Image%20of%20Streamlit%20(Python)%20Karaoke%20Singer%20Registration%20web%20application.jpg"  width="350" height="250">
</p>

Took part in a 7-day general programming SUTD Freshmore Freshmore Asian Cross-curricular Trip (FACT) to Petra Christian University (PCU) in Surabaya, Indonesia as part of the 10.020 Data Driven World module. Took part in the hackathon during the trip in a team of 6 (3 SUTD students and 3 PCU students) and achieved 1st Place (out of 10 teams).

From the [SUTD FACT Trips official website](https://www.sutd.edu.sg/campus-life/global-experience-and-exchange/sutd-fact/): 'FACT (Freshmore Asian Cross-curricular Trips) is a 1-week overseas immersion programme which enables Freshmore (first-year) students to build upon their acquired knowledge at our partner universities in Asia. Centered around specific Freshmore courses, FACT challenges students to apply what they’ve learned in the classroom to solving sustainability challenges within the region.'

The challenge of this hackathon was to create a website application using Streamlit and machine learning to help local businesses (we visited a cafe, paving factory and farm) in Gunung Anyar, Surabaya, Indonesia.

Created a functional prototype Streamlit website application to help out a local farm business (particularly about finding the optimal conditions for hydroponic farming of spinaches), titled '**TaniBoss!**' ('Tani' comes from 'Petani', which is Indonesian for 'Farmer'). It contains the features:
- A simple prediction and farming conditions recommendation machine learning model to optimise crop yield

  This 
- A forum for local farmers
- PetaniAI, a large language model trained with hydroponic and general farming data (using the Chatbase custom GPT LLM model API) to serve as a secondary expert

Contributed to the problem statemenet formulation, design of the machine learning model, and development of the Streamlit website (including the forum and PetaniAI features).

**Potential Improvements:**  
(TaniBoss! is only a functional prototype and a proof of concept, hence some of the features is only shown as UI and doesnt actually work)  
- Currently the forum feature in TaniBoss! is not connected to any database, hence questions and answers posted on the forum will not be saved and will all be deleted whenever TaniBoss! is rerun.
- PetaniAI was created and trained using the Chatbase custom GPT LLM model API, which requires a paid subscription to maintain. However, I have stopped subscription and hence PetaniAI no longer works and will not be able to generate responses from prompts anymore
- Since the prediction and farming conditions recommendation machine learning model is trained from a static database (the [Crop yield dataset CSV file](hi)) (add link!), rather than a realtime database, it does not actually take in new data input from the local farmers and retrain itself to update its parameters... (the inputs to 'Train the Model' in the 'Predictor' page in TaniBoss! does not actually do anything and is just shown as UI)

**Additional source(s):**  
nil

*This project's deployed Streamlit (Python Framework)'s Web Application link:*
+ https://8kbtr2cyktbh4qn2doay5g.streamlit.app/ 

<br>

## Table of Contents
Here is a directory to explain the purpose of each file in this repository:

1. [Files that are required in the creation of the Streamlit Web Application Project - TaniBoss!](#filesrequiredincreationofstreamlitwebapplications)
    1. '.streamlit' folder  
       i. 'config.toml' file
    2. 'README.md' file
    3. 'Crop yield dataset.csv' file
    4. 'Image of PetaniAI logo.jpg', 'Image of PetaniAI user logo.jpg', 'Image of local hydroponic farm site analysis.jpg' and 'Image of plant diseases.jpg' files
    5. 'main.py' file
    6. 'requirements.txt' file
    
2. [Deployment Process of the Streamlit and Firebase Web Application Project for TaniBoss! on Streamlit Cloud](#deploymentofstreamlitwebapplications)

<br>

## 1. Files that are required in the creation of the Streamlit and Firebase Web Application Project for a Karaoke Event <a name = "filesrequiredincreationofstreamlitwebapplications"></a>
**1. '.streamlit' folder**  
*i. config.toml' file*
```python
# This 'config.toml' file sets the custom theming of the Streamlit (Python) web applications. This file is created using ChatGPT.
[theme]
primaryColor = '#1a237e'  # Set your desired primary color
backgroundColor = '#121212'  # Set your desired background color
secondaryBackgroundColor = '#0d47a1'  # Set your desired secondary background color
textColor = '#ffffff'  # Set your desired text color
font = 'sans-serif'  # Set your desired font
```
This is an optional folder/file, in accordance to the deployment of Streamlit (Python Framework) Web Application documentation: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app (Streamlit Cloud), which allows you to set customised configurations or themings to the deployed Streamlit (Python Framework) Web Application.

I do not know how to use this 'config.toml' file very proficiently, so this file is created by ChatGPT to set the dark theming to my 2 deployed Streamlit (Python Framework) Web Applications.

<br>

**2. 'README.md' file**  
The 'README.md' file.

<br>

**3. 'firebase_key.json' file**
```python

```
This file represents the authetication key. Apparently, when accessing to APIs (such as the Firebase API), you will need to have a sort of, authentication key, which is what this file is to ensure that only authorized users can access the API. Refer to this video to understand how the Firebase API authentication key is used with your Python code: https://www.youtube.com/watch?v=s-Ga8c3toVY&t=336s (Code First with Hala) 

<br>

**4. 'Image of PetaniAI logo.jpg', 'Image of PetaniAI user logo.jpg', 'Image of local hydroponic farm site analysis.jpg' and 'Image of plant diseases.jpg' files**
<p align="center"> 
  <img src="https://github.com/WindJammer6/18.-Deployed-Streamlit-Python-and-Firebase-Web-Application-Project-for-a-Karaoke-Event/blob/main/README%20images/karaoke_poster.jpg"  width="450" height="200">
  <img src="https://github.com/WindJammer6/18.-Deployed-Streamlit-Python-and-Firebase-Web-Application-Project-for-a-Karaoke-Event/blob/main/README%20images/karaoke_poster.jpg"  width="450" height="200">
  <img src="https://github.com/WindJammer6/18.-Deployed-Streamlit-Python-and-Firebase-Web-Application-Project-for-a-Karaoke-Event/blob/main/README%20images/karaoke_poster.jpg"  width="450" height="200">
  <img src="https://github.com/WindJammer6/18.-Deployed-Streamlit-Python-and-Firebase-Web-Application-Project-for-a-Karaoke-Event/blob/main/README%20images/karaoke_poster.jpg"  width="450" height="200">
</p>
Images used for aesthetic purposes in the TaniBoss! Streamlit (Python Framework) Web Application.

<br>

**5. 'main.py' file**  
The main Python file for the TaniBoss! Streamlit (Python Framework) Web Application itself.

<br>

**6. 'requirements.txt' file**
```python
streamlit           
numpy
# streamlit_extras
pandas
scikit-learn
requests
datetime
matplotlib
```
This is a compulsory file, in accordance to the deployment of Streamlit (Python Framework) Web Application documentation: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app (Streamlit Cloud), which allows you to tell Streamlit (Python Framework) to download the necessary external libraries/framework/packages specified in this 'requirements.txt' file in the deployment environment that is required for the deployment of the Streamlit (Python Framework) Web Application. 

Had quite the trouble during deployment of the Streamlit (Python Framework) Web Applications as the Streamlit deployment platform keep giving an error that it could not find the relevant external libraries/Framework/packages required to deploy my Streamlit (Python Framework) Web Applications until I found out in the deployment of Streamlit (Python Framework) Web Application documentation: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app (Streamlit Cloud) that apparently I needed this seperate 'requirements.txt' file in order to tell the Streamlit deployment platform to download the necessary external libraries/framework/packages during the deployment of the Streamlit (Python Framework) Web Applications.

Apparently, the 'requirements.txt' file is a common practice across various deployment platforms in Python, not just for Streamlit (Python Framework) Cloud. Whether you are deploying your Streamlit app on platforms like Heroku, AWS, Vercel, or others, specifying dependencies in a 'requirements.txt' file allows the platform to understand and install the necessary packages.

<br>

## 2. Deployment Process of the Streamlit and Firebase Web Application Project for TaniBoss! on Streamlit Cloud <a name = "deploymentofstreamlitwebapplications"></a> ![My Skills](https://go-skill-icons.vercel.app/api/icons?i=streamlit)

*What is [Streamlit Cloud](https://streamlit.io/cloud)?*  
From the official [Streamlit Cloud](https://streamlit.io/cloud) website: 'Streamlit Cloud is a new product that lets you build, deploy, and share data from Streamlit Web Applications in minutes.' 

Honestly, the documentation on how to deploy a Streamlit (Python Framework) Web Application on Streamlit Cloud (link: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app) explains very clearly step by step on how to deploy a Streamlit Web Application on [Streamlit Cloud](https://streamlit.io/cloud). Once deployed correctly, I got a direct 'streamlit.io' link to the Streamlit Web Application, which I can then share with others to try out this Streamlit Web Application.

<br>  

- Here is the link of my [Streamlit Cloud](https://streamlit.io/cloud) account of the username: 'WindJammer6' - https://share.streamlit.io/user/windjammer6
- Here is the link of this deployed Streamlit Web Application using [Streamlit Cloud](https://streamlit.io/cloud)
    - 

Source(s):  
+ https://streamlit.io/cloud (Streamlit Cloud)
+ https://blog.streamlit.io/introducing-streamlit-cloud/ (Streamlit Blog)
+ https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app (Streamlit Cloud) (Documentation on how to deploy a Streamlit (Python Framework) Web Application on Streamlit Cloud)
