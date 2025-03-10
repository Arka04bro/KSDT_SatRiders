Welcome to the **SatRiders** team repository for the **KAZ ROCKETS Satellite Design Tournament**! 🚀  
Here, you'll find all the code, documentation, and details about our machine learning model.  

---

## 🤖 Machine Learning Concept

### Why Ensemble Learning? 🤔
We chose **Ensemble Learning** because of its superior accuracy and robustness.  
Ensemble learning is a machine learning technique that combines multiple models (e.g., regression models, neural networks) to produce better predictions than any single model alone. By aggregating the predictions of several models, we can reduce errors and improve overall performance.  
![image](https://github.com/user-attachments/assets/3c5adb4b-7fe8-4236-ad9d-243487a0b91f)

---

## 🧠 How Our Model Works

Our machine learning model is designed to analyze satellite data and predict environmental factors such as pollution levels, wind patterns, and topography. Here's how it works:

1. **Data Collection**: We gather data from various sensors, including gas concentrations, wind speed, wind direction, temperature, and humidity.
2. **Preprocessing**: The data is cleaned, normalized, and prepared for analysis.
3. **Ensemble Model**: We use a combination of models (e.g., Random Forest, Gradient Boosting, Neural Networks) to make predictions.
4. **Output**: The model generates predictions for pollution levels, wind patterns, and other environmental factors.
   
<img width="418" alt="{83DFC1C9-8EBA-4B61-883C-1F9ABA73A59F}" src="https://github.com/user-attachments/assets/c7574b5a-e6bc-4ad4-b907-6700f4552975" />

---

## 📊 Output Data

Our model produces the following outputs:
- **Pollution Levels**: Predicted gas concentrations in different areas.
- **Wind Patterns**: Wind speed and direction (visualized as a wind rose 🌹).
- **Topography**: Information about the terrain (e.g., forest, grassland, hills).
- **Accuracy Metrics**: Precision, recall, and F1-score to evaluate model performance.
  ![image](https://github.com/user-attachments/assets/0c2a3c04-5e60-442f-86b6-b3ca9acde34f)
![image](https://github.com/user-attachments/assets/6e946c03-1d65-4e76-a790-5d457094f6ec)

<img width="517" alt="{F37DD459-DF7C-405A-9742-FD61B1FA5342}" src="https://github.com/user-attachments/assets/982d1f9e-8dea-4f58-8044-174bd9b62219" />

---

## 🗺️ Folium Map Visualization

We use **Folium** to create interactive maps that visualize pollution levels and other environmental data.  
- **Heatmaps**: Show areas with high pollution levels (🔥 red for high, 🟢 green for low).
- **Markers**: Indicate specific data points collected by the satellite.
- **Wind Rose**: Visualizes wind patterns using directional data.

---

## 🌹 Wind Rose

The **Wind Rose** is a graphical representation of wind patterns. It shows:
- **Wind Direction**: The direction from which the wind is blowing (e.g., N, NE, E).
- **Wind Speed**: The intensity of the wind at different directions.

---

## 🎯 Model Accuracy

Our ensemble model achieves high accuracy due to the following:
- **Combination of Models**: By combining multiple models, we reduce bias and variance.
- **Cross-Validation**: We use cross-validation to ensure the model generalizes well to unseen data.
- **Metrics**: We evaluate the model using precision, recall, and F1-score.
  

---

## 🧮 Mathematics Behind the Model

The core mathematical concepts used in our model include:
- **Ensemble Averaging**: Combining predictions from multiple models to reduce errors.
- **Gradient Boosting**: Minimizing loss functions by iteratively improving weak learners.
- **Random Forest**: Using decision trees with random subsets of data to prevent overfitting.
- **Neural Networks**: Leveraging layers of neurons to capture complex patterns in the data.

---
## 🧢 Arduino code
We have optimized our code by using seven functions and creating dedicated custom functions for each sensor. You can view and download the code.
Additionally, we have included eight libraries in our project, such as:
TinyGPS
Wire.h
Adafruit_BMP085
Adafruit_MPU6050
These are the core libraries we used to ensure efficient and structured development.
<img width="317" alt="{129C9ADB-90F0-49D6-AA50-320847FBA749}" src="https://github.com/user-attachments/assets/e37a39b7-200c-43a6-9277-7c9345867ea6" />

 We used an Arduino Uno as the main data collection unit. The entire system is powered by a 3.7V lithium battery, followed by a step-up converter to 5V. The sensors used in the system include: three gas sensors, a pressure sensor, a 9-axis accelerometer, an I2C multiplexer, an SD card module, and a GPS module.

---
## 🚀 Get Started

To run the code and visualize the results:
1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
