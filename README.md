# Climate-Cast

Climate-Cast is a web application that provides climate data analysis and prediction capabilities. The application offers temperature trend visualization, rainfall prediction, and temperature prediction features through an interactive web interface.

## Features

- **Temperature Analysis Dashboard**
  - Visualizes temperature trends over years
  - Displays key statistics including:
    - Latest year's data
    - Current average temperature
    - Maximum and minimum temperatures


- **Temperature Prediction**
  - Predicts temperature based on:
    - Rainfall
    - Wind speed
    - Selected month

## Technologies Used

- **Backend**
  - Python
  - Flask (Web Framework)
  - Pandas (Data Processing)
  - Plotly (Data Visualization)

- **Frontend**
  - HTML/CSS
  - JavaScript
  - Plotly.js

## Installation

1. Clone the repository
2. Install the required dependencies:
```bash
pip install flask pandas plotly
```
3. Run the application:
```bash
python app.py
```
4. Open your web browser and navigate to `http://localhost:5000`

## Project Structure

```
├── app.py              # Main Flask application
├── dataset.csv         # Climate data
├── static/             # Static files (CSS)
│   ├── monitor.css
│   └── styles.css
├── templates/          # HTML templates
│   ├── about.html
│   ├── base.html
│   ├── index.html
│   ├── monitor.html
│   ├── predict_rainfall.html
│   └── predict_temperature.html
└── train.ipynb         # Model training notebook
```

## Usage

1. **View Temperature Analysis**
   - Navigate to the home page to view the temperature trends and statistics

2. **Predict Temperature**
   - Go to the Temperature Prediction page
   - Enter rainfall and wind speed
   - Select a month
   - Click "Predict Temperature" to get the prediction


        
