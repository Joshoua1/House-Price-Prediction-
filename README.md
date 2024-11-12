# House Price Prediction Application

This is a web application that predicts house prices based on various features such as living area, number of bedrooms, and more. The application uses machine learning algorithms to provide accurate price predictions.

## Features

- Basic and advanced prediction modes.
- User-friendly interface with Bootstrap for responsive design.
- Interactive forms that dynamically display fields based on user selection.
- Real-time predictions displayed after form submission.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **Pandas**: A data manipulation and analysis library for Python.
- **XGBoost**: An optimized distributed gradient boosting library designed to be highly efficient.
- **Bootstrap**: A front-end framework for developing responsive and mobile-first websites.
- **HTML/CSS/JavaScript**: Standard web technologies for structuring and styling the application.

## Installation

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/Joshoua1/House-Price-Prediction-.git
cd house-price-prediction
```

### Install Required Packages
Create a virtual environment (recommended) and install the required packages:

```bash
# Create a virtual environment (optional)
python -m venv venv
# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install required packages
pip install Flask pandas xgboost scikit-learn
```

### Data File

Make sure to place the House Price India.csv data file in the same directory as app.py. This file should contain the relevant data used for training the model.
Running the Application

### To run the application, use the following command:

```bash
python app.py
```

Open your web browser and navigate to http://127.0.0.1:5000/ to access the application.

Usage
1. Select either "Basic" or "Advanced" prediction mode.
2. Fill in the required fields based on your selection.
3. Click the "Predict Price" button to see the predicted house price.

### Contributing

Contributions are welcome! If you have suggestions for improvements or features, feel free to create an issue or submit a pull request.
