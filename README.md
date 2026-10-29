🚦 Intelligent Traffic Management System using AI/ML
An AI/ML-based traffic management prototype that predicts traffic congestion levels and provides smart traffic signal recommendations based on current traffic conditions.

📌 Project Overview
The Intelligent Traffic Management System is designed to assist in managing traffic congestion using Machine Learning.

The system takes traffic-related inputs such as:
- 🕐 Hour of the day
- 📅 Day type
- 🌦️ Weather condition
- 🚗 Number of vehicles in different lanes
- 🏎️ Average vehicle speed
- 🚑 Emergency vehicle status

These inputs are processed by a Random Forest Classifier, which predicts the congestion level as:
Low | Medium | High | Severe
Based on the predicted congestion, the system recommends suitable green-signal timing and identifies the busiest lane. Emergency vehicles are also given priority in the decision logic.

---

🎯 Objectives
- Predict traffic congestion using Machine Learning.
- Identify the lane with the highest traffic volume.
- Recommend suitable green-signal timing.
- Provide priority to emergency vehicles.
- Create an interactive dashboard for traffic analysis.
- Demonstrate how AI/ML can support intelligent traffic management.

---

🧠 Machine Learning Model

Algorithm Used
Random Forest Classifier
Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees to make predictions.

Problem Type
Classification
The model classifies traffic conditions into four categories:
- Low
- Medium
- High
- Severe

Input Features
Feature| Description
Hour| Hour of the day
Day Type| Weekday / Weekend
Weather| Clear / Rain / Fog
Emergency Vehicle| Yes / No
Lane 1 Vehicles| Vehicle count in Lane 1
Lane 2 Vehicles| Vehicle count in Lane 2
Lane 3 Vehicles| Vehicle count in Lane 3
Lane 4 Vehicles| Vehicle count in Lane 4
Average Speed| Average vehicle speed

Target

"congestion_level"

---

🏗️ System Architecture

Traffic Input
     ↓
Data Preprocessing
     ↓
Random Forest Classifier
     ↓
Congestion Prediction
     ↓
Traffic Decision Logic
     ↓
 ┌──────────────────────────────┐
 │ Busiest Lane                │
 │ Recommended Green Time      │
 │ Emergency Vehicle Priority  │
 └──────────────────────────────┘
     ↓
Streamlit Dashboard

---

🖥️ Application Features

1. Traffic Congestion Prediction
Predicts the current traffic congestion level using the trained Random Forest model.

2. Traffic Analysis
Calculates total vehicles and identifies the busiest lane.

3. Smart Signal Recommendation
Suggests green-signal timing according to the predicted congestion level.

4. Emergency Vehicle Priority
If an emergency vehicle is detected, the system prioritizes traffic movement by recommending higher green time.

5. Interactive Dashboard
The complete system is implemented using Streamlit, allowing users to enter traffic conditions and view results interactively.

6. Visual Traffic Representation
The dashboard displays vehicle distribution across lanes using a graph.

---

🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn
- Random Forest Classifier
- Streamlit
- Joblib
- Matplotlib

---

📂 Project Structure
Intelligent-Traffic-Management-AI/
│
├── app.py
├── train_model.py
├── traffic_data.csv
├── traffic_model.pkl
├── requirements.txt
├── README.md
└── .gitignore

---

⚙️ Installation & Setup

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/Intelligent-Traffic-Management-AI.git

2. Open the project folder

cd Intelligent-Traffic-Management-AI

3. Install dependencies

pip install -r requirements.txt

4. Run the Streamlit application

streamlit run app.py

The application will open in your browser.

---

📊 Dataset

For this academic prototype, a synthetic/demo traffic dataset is used for training and testing the Machine Learning model.

The dataset contains different combinations of traffic conditions, vehicle counts, average speed, weather, time and emergency-vehicle status.

«Note: This project currently does not use live CCTV feeds, real-time traffic sensors or live traffic APIs.»

---

🚀 Future Scope

The system can be further improved by integrating:

- 📹 Real-time CCTV camera feeds
- 🚦 Automatic adaptive traffic signals
- 📡 IoT-based traffic sensors
- 🗺️ GPS and live traffic data
- 🚑 Real-time ambulance/emergency vehicle tracking
- 🤖 Computer Vision for vehicle detection
- 📈 Real-time traffic prediction
- 🚨 Accident and unusual-traffic detection

---

⚠️ Current Limitation

This is an academic prototype and decision-support system. The current version provides traffic recommendations through a Streamlit dashboard but does not directly control physical traffic signals.

---

👩‍💻 Developed By

Kajal Singh
B.Tech Computer Science & Engineering

---

⭐ Key Learning Outcomes

Through this project, I worked with:

- Machine Learning classification
- Random Forest
- Data preprocessing
- Feature engineering
- Model training and evaluation
- Python and Pandas
- Streamlit application development
- Integrating a trained ML model with a user interface
- Building a complete end-to-end ML project

---

📌 Project Status

Completed — Academic Prototype
