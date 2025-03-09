# 🛰️ KSDT_SatRiders

Welcome to the **SatRiders** team repository for the **KAZ ROCKETS Satellite Design Tournament**! 🚀  
Here, you'll find all the code, documentation, and details about our machine learning model.  

---

## 🤖 Machine Learning Concept

### Why Ensemble Learning? 🤔
We chose **Ensemble Learning** because of its superior accuracy and robustness.  
Ensemble learning is a machine learning technique that combines multiple models (e.g., regression models, neural networks) to produce better predictions than any single model alone. By aggregating the predictions of several models, we can reduce errors and improve overall performance.  

---

## 🧠 How Our Model Works

Our machine learning model is designed to analyze satellite data and predict environmental factors such as pollution levels, wind patterns, and topography. Here's how it works:

1. **Data Collection**: We gather data from various sensors, including gas concentrations, wind speed, wind direction, temperature, and humidity.
2. **Preprocessing**: The data is cleaned, normalized, and prepared for analysis.
3. **Ensemble Model**: We use a combination of models (e.g., Random Forest, Gradient Boosting, Neural Networks) to make predictions.
4. **Output**: The model generates predictions for pollution levels, wind patterns, and other environmental factors.

---

## 📊 Output Data

Our model produces the following outputs:
- **Pollution Levels**: Predicted gas concentrations in different areas.
- **Wind Patterns**: Wind speed and direction (visualized as a wind rose 🌹).
- **Topography**: Information about the terrain (e.g., forest, grassland, hills).
- **Accuracy Metrics**: Precision, recall, and F1-score to evaluate model performance.

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

## 🚀 Get Started

To run the code and visualize the results:
1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
