# 18.-TaniBoss! 
<p align="center"> 
  <img src="https://github.com/WindJammer6/18.-Deployed-Streamlit-Python-and-Firebase-Web-Application-Project-for-a-Karaoke-Event/blob/main/README%20images/Image%20of%20Streamlit%20(Python)%20Karaoke%20Singer%20Registration%20web%20application.jpg"  width="350" height="250">
</p>

Took part in a 7-day general programming SUTD Freshmore Freshmore Asian Cross-curricular Trip (FACT) to Petra Christian University (PCU) in Surabaya, Indonesia as part of the 10.020 Data Driven World module. Took part in the hackathon during the trip in a team of 6 (3 SUTD students and 3 PCU students) and achieved 1st Place (out of 10 teams).

From the SUTD FACT Trips official website: 'FACT (Freshmore Asian Cross-curricular Trips) is a 1-week overseas immersion programme which enables Freshmore (first-year) students to build upon their acquired knowledge at our partner universities in Asia. Centered around specific Freshmore courses, FACT challenges students to apply what they’ve learned in the classroom to solving sustainability challenges within the region.'

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
- https://docs.streamlit.io/library/api-reference/session-state (Streamlit) (Streamlit (Python Framework)'s official documentation on it's 'st.session_state' function. Had a seperate learning source for this particular function due to the complexity of its function)  
- https://www.youtube.com/watch?v=92jUAXBmZyU (Streamlit) (Youtube Video: 'Session State Basics' by Streamlit)  
- https://github.com/kmcgrady/streamlit-autorefresh#how-does-this-component-help ([kmcgrady](https://github.com/kmcgrady) on Github) (Documentation on a custom Streamlit function, 'st_autorefresh' from the custom  'streamlit-autorefresh' library created by [kmcgrady](https://github.com/kmcgrady) that I used in the song queue display Streamlit (Python Framework) Web Application)
- https://chat.openai.com/ (ChatGPT)  
- And lastly... seniors and friends from school :)

<br>

## My Approach to developing this UROP project:  
The approach to developing this UROP project is split into 3 components:  
2 Web Applications using Streamlit (Python Framework), linked together via 1 Firebase (API)'s Realtime Database. The first Web Application allows users to submit their name and song choice via a Streamlit (Python) website link, where the data will then be added into the Firebase (API)'s Realtime Database, where the other Streamlit (Python) Web Application will draw the data from to display the data in a song queue on a projected screen during the Karaoke Event to show whoever is the next singer and their song choice.

*This project's deployed Streamlit (Python Framework)'s Web Applications and Firebase (API) links:*
+ https://8kbtr2cyktbh4qn2doay5g.streamlit.app/ (Karaoke Singer Registration Streamlit (Python Framework) Web Application)
+ https://2bgope7myic8tuh3dy6vi4.streamlit.app/ (Song queue display Streamlit (Python Framework) Web Application)
+ https://console.firebase.google.com/u/0/project/karaokeeventproject/database/karaokeeventproject-default-rtdb/data (Direct link to this project's Firebase (API) Realtime database, but only accessible by me through email)  

<br>

## Table of Contents
Here is a directory to explain the purpose of each file in this repository:

1. [Files that are required in the creation of the Streamlit and Firebase Web Application Project for a Karaoke Event](#filesrequiredincreationofstreamlitwebapplications)
    1. '.streamlit' folder  
       i. 'config.toml' file
    2. 'README.md' file
    3. 'firebase_key.json' file
    4. 'karaoke_poster.jpg' file
    5. 'karaoke_singer_class.py' file
    6. 'queue_data_structure_class.py' file
    7. 'register.py' file
    8. 'requirements.txt' file
    9. 'song_queue.py' file
      
2. [Additional files that are not part of the creation of the Streamlit and Firebase Web Application Project for a Karaoke Event, but includes the past iterations/versions/prototypes of the Streamlit and Firebase Web Application Project for a Karaoke Event](#filesofpastiterationsofstreamlitwebapplications)
    1. (main, using Firebase as database) Streamlit (Python Framework) and Firebase ROOTech Karaoke Night project
    2. (prototype, using csv file as database) Streamlit (Python Framework) ROOTech Karaoke Night project
  
3. [Additional files that are not part of the creation of the Streamlit and Firebase Web Application Project for a Karaoke Event, but includes my learning journey of some of the required technology being used in this project that I was not familiar with](#filesoflearningjourney)
    1. Streamlit (Python Framework) learn
    2. Firebase (Python Framework) learn
    
4. [Deployment Process of the Streamlit and Firebase Web Application Project for a Karaoke Event on Streamlit Cloud](#deploymentofstreamlitwebapplications)

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

**4. 'karaoke_poster.jpg' file**
<p align="center"> 
  <img src="https://github.com/WindJammer6/18.-Deployed-Streamlit-Python-and-Firebase-Web-Application-Project-for-a-Karaoke-Event/blob/main/README%20images/karaoke_poster.jpg"  width="450" height="200">
</p>
An image used for aesthetic purposes in the song registration Streamlit (Python Framework) Web Application.

<br>

**5. 'karaoke_singer_class.py' file**
```python
class KaraokeSinger:
    def __init__(self, name, song_choice, song_artist):
        self.name = name
        self.song_choice = song_choice
        self.song_artist = song_artist

    #Just want to be able to see the 'KaraokeSinger' object's attribute in the terminal when it is printed rather than
    #a 'KaraokeSinger' object
    def __repr__(self):
        return "KaraokeSinger('{}', '{}', '{}')".format(self.name, self.song_choice, self.song_artist)
    
    #Allows the 'KaraokeSinger' object to be recreated as a dictionary so it can be used to be reuploaded into the csv 
    #database in 'karaoke_singer_registration_streamlit.py' file
    def as_dict(self):
        return {'name': self.name, 'song_choice': self.song_choice, 'song_artist': self.song_artist}
```
A supporting OOP Python 'Karaoke Singer' class file used in building the project. 

<br>

**6. 'queue_data_structure_class.py' file**
```python
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,value):
        self.buffer.appendleft(value)

    def dequeue(self):
        return self.buffer.pop()

    def front_element(self):
        return self.buffer[-1]
    
    def last_element(self):
        return self.buffer[0]
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def __repr__(self):
        return '{}'.format(self.buffer)
```
A supporting OOP Python Queue Data Structure class file used in building the project, for the song queue Streamlit (Python Framework) Web Application.

<br>

**7. 'register.py' file**  
The main Python file for the song registration Streamlit (Python Framework) Web Application itself.

<br>

**8. 'requirements.txt' file**
```python
firebase_admin
streamlit_autorefresh
```
This is a compulsory file, in accordance to the deployment of Streamlit (Python Framework) Web Application documentation: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app (Streamlit Cloud), which allows you to tell Streamlit (Python Framework) to download the necessary external libraries/framework/packages specified in this 'requirements.txt' file in the deployment environment that is required for the deployment of the Streamlit (Python Framework) Web Application. 

Had quite the trouble during deployment of the Streamlit (Python Framework) Web Applications as the Streamlit deployment platform keep giving an error that it could not find the relevant external libraries/Framework/packages required to deploy my Streamlit (Python Framework) Web Applications until I found out in the deployment of Streamlit (Python Framework) Web Application documentation: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app (Streamlit Cloud) that apparently I needed this seperate 'requirements.txt' file in order to tell the Streamlit deployment platform to download the necessary external libraries/framework/packages during the deployment of the Streamlit (Python Framework) Web Applications.

Apparently, the 'requirements.txt' file is a common practice across various deployment platforms in Python, not just for Streamlit (Python Framework) Cloud. Whether you are deploying your Streamlit app on platforms like Heroku, AWS, Vercel, or others, specifying dependencies in a 'requirements.txt' file allows the platform to understand and install the necessary packages.

<br>

**9. 'song_queue.py' file**  
The main Python file for the song queue Streamlit (Python Framework) Web Application itself.

<br>

Source(s):  
- https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app (Streamlit Cloud) (Documentation on how to deploy a Streamlit (Python Framework) Web Application on Streamlit Cloud)
- https://www.youtube.com/watch?v=s-Ga8c3toVY&t=336s (Code First with Hala) 
 
<br>

## 2. Past iterations/versions/prototypes of the Streamlit and Firebase Web Application Project for a Karaoke Event <a name = "filesofpastiterationsofstreamlitwebapplications"></a>
1. *(main, using Firebase as database) Streamlit (Python Framework) and Firebase ROOTech Karaoke Night project*  
   Consists of the files that contains the code for the main version of the Streamlit (Python Framework) Web Application Project with the Firebase (API). (excludes the supporting files required for deployment of the Streamlit (Python Framework) and Firebase (API) Web Application Project with detailed namings of the files)

<br>

2. *(prototype, using csv file as database) Streamlit (Python Framework) ROOTech Karaoke Night project*  
    Consists of the files that contains the prototype version of the Streamlit (Python Framework) Web Application Project, but it uses a CSV file as a 'database' rather than the Firebase (API). However, a senior eventually mentioned that this will not work as a CSV file is not dynamic, and will be unchangable/static when it is deployed, which will not work as the project needs to be dynamic, where the database needs to be able to be constantly updated during the deployment. This is where the connecting the 2 Streamlit Web Applications to an alternate database such as Firebase (API)'s Realtime Database solves the problem.

<br>

## 3. My learning journey of some of the required technology being used in this project that I was not familiar with <a name = "filesoflearningjourney"></a>
Due to my lack of knowledge in some of the required technology being used in the Streamlit and Firebase Web Application Project for a Karaoke Event , I had to first learn them, which includes:
1. *Streamlit (Python Framework) learn  
   Consists of my learning journey of the Streamlit Python Framework.

   *What is Streamlit (Python Framework)?*  
   Streamlit is a Python Framework for developing Web Applications especially for Data Science, Machine Learning and Artificial Intelligence.

Source(s):  
- https://www.youtube.com/playlist?list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW (Nileg Production) (Youtube playlist by Nileg Production titled 'Python Streamlit Full Course') (only up till the 14th video in the playlist)

<br>

2. *Firebase (Python Framework) learn*  
    Consists of my learning journey of the Firebase Python Framework.

   *What is Firebase (Python Framework)?*  
   Firebase is a platform provided by Google for building web and mobile applications. It offers a wide range of services and tools that help developers create high-quality applications more easily and efficiently. One of the services provided by Firebase is the Realtime Database, which is a NoSQL cloud-hosted database that allows you to store and synchronize data in real-time.

   It is a seperate software, but you can use the Firebase Python library, 'firebase_admin' to integrate functionality of this seperate Firebase software into your Python projects to allow you to allow your Python projects here to interact with your seperate backend Firebase software.

Source(s):  
- https://console.firebase.google.com/ (Firebase) (Firebase console/dashboard)
- https://www.youtube.com/watch?v=s-Ga8c3toVY&t=336s (Code First with Hala) (Youtube video by Code First with Hala titled, 'Firebase Python FULL COURSE: Authentication, Storage, Realtime Database CRUD tutorials (pyrebase)')

<br>

## 4. Deployment Process of the Streamlit and Firebase Web Application Project for a Karaoke Event on Streamlit Cloud <a name = "deploymentofstreamlitwebapplications"></a> ![My Skills](https://go-skill-icons.vercel.app/api/icons?i=streamlit)

*What is [Streamlit Cloud](https://streamlit.io/cloud)?*  
From the official [Streamlit Cloud](https://streamlit.io/cloud) website: 'Streamlit Cloud is a new product that lets you build, deploy, and share data from Streamlit Web Applications in minutes.' 

Honestly, the documentation on how to deploy a Streamlit (Python Framework) Web Application on Streamlit Cloud (link: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app) explains very clearly step by step on how to deploy a Streamlit Web Application on [Streamlit Cloud](https://streamlit.io/cloud). Once deployed correctly, I got a direct 'streamlit.io' link to the Streamlit Web Application, which I can then share with others to try out this Streamlit Web Application.

<br>  

- Here is the link of my [Streamlit Cloud](https://streamlit.io/cloud) account of the username: 'WindJammer6' - https://share.streamlit.io/user/windjammer6
- Here are the links of this deployed Streamlit Web Application using [Streamlit Cloud](https://streamlit.io/cloud)
    - https://8kbtr2cyktbh4qn2doay5g.streamlit.app/ (Karaoke Singer Registration Streamlit (Python Framework) Web Application)
    - https://2bgope7myic8tuh3dy6vi4.streamlit.app/ (Song queue display Streamlit (Python Framework) Web Application)

Source(s):  
+ https://streamlit.io/cloud (Streamlit Cloud)
+ https://blog.streamlit.io/introducing-streamlit-cloud/ (Streamlit Blog)
+ https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app (Streamlit Cloud) (Documentation on how to deploy a Streamlit (Python Framework) Web Application on Streamlit Cloud)














Check out the project here! 
-> https://github.com/WindJammer6/17.-Mini-Projects-from-School

- Took part in this 7-day general programming FACT trip to Petra Christian University (PCU) in Surabaya, Indonesia as part of the 10.020 Data Driven World module. Took part in the hackathon during the trip in a team of 6 (3 SUTD students and 3 PCU students) and achieved 1st Place (out of 10 teams)
- From the SUTD FACT Trips official website: 'FACT (Freshmore Asian Cross-curricular Trips) is a 1-week overseas immersion programme which enables Freshmore (first-year) students to build upon their acquired knowledge at our partner universities in Asia. Centered around specific Freshmore courses, FACT challenges students to apply what they’ve learned in the classroom to solving sustainability challenges within the region.'
- The challenge of this hackathon was to create a website application using Streamlit and machine learning to help local businesses (we visited a cafe, paving factory and farm) in Gunung Anyar, Surabaya, Indonesia
- Created a functional prototype Streamlit website application to help out a local farm business (particularly about finding the optimal conditions for hydroponic farming of spinaches), titled 'TaniBoss!' ('Tani' comes from 'Petani', which is Indonesian for 'Farmer'). It contains a simple prediction and farming conditions recommendation machine learning model to optimise crop yield, a forum for farmers, and PetaniAI, a large language model trained with hydroponic and general farming data (using Chatbase) to serve as a secondary expert. 
- Contributed to the problem statemenet formulation, design of the machine learning model, and development of the Streamlit website (including the forum and PetaniAI features)
