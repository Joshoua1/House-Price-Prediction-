from flask import Flask, render_template, request
import pandas as pd
from xgboost import XGBRegressor

# Load your data and train models here (as in your provided code)
data = pd.read_csv("House Price India.csv")
data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')

# Define features
basic_features = ['living_area', 'grade_of_the_house', 'area_of_the_house(excluding_basement)']
advanced_features = ['living_area', 'grade_of_the_house', 'area_of_the_house(excluding_basement)',
                    'number_of_bedrooms', 'number_of_bathrooms', 'lot_area', 
                    'number_of_floors', 'waterfront_present',
                    'condition_of_the_house', 'area_of_the_basement', 
                    'built_year']

# Train models
def train_model(features):
    X = data[features]
    y = data['price']
    model = XGBRegressor()
    model.fit(X, y)
    return model

basic_model = train_model(basic_features)
advanced_model = train_model(advanced_features)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_price = None
    if request.method == 'POST':
        mode = request.form.get('mode')
        input_data = {}
        
        if mode == 'basic':
            input_data['living_area'] = float(request.form['living_area'])
            input_data['grade_of_the_house'] = int(request.form['grade_of_the_house'])
            input_data['area_of_the_house(excluding_basement)'] = float(request.form['area_of_the_house(excluding_basement)'])
            features = basic_features
            model = basic_model
            
        elif mode == 'advanced':
            input_data['living_area'] = float(request.form['living_area'])
            input_data['grade_of_the_house'] = int(request.form['grade_of_the_house'])
            input_data['area_of_the_house(excluding_basement)'] = float(request.form['area_of_the_house(excluding_basement)'])
            input_data['number_of_bedrooms'] = int(request.form['number_of_bedrooms'])
            input_data['number_of_bathrooms'] = int(request.form['number_of_bathrooms'])
            input_data['lot_area'] = float(request.form['lot_area'])
            input_data['number_of_floors'] = int(request.form['number_of_floors'])
            input_data['waterfront_present'] = int(request.form['waterfront_present'])
            input_data['condition_of_the_house'] = int(request.form['condition_of_the_house'])
            input_data['area_of_the_basement'] = float(request.form.get('area_of_the_basement', 0))  # Default to 0 if not provided
            input_data['built_year'] = int(request.form.get('built_year', 0))  # Default to 0 if not provided
            
            features = advanced_features
            model = advanced_model
        
        # Create DataFrame for prediction
        input_df = pd.DataFrame([input_data], columns=features)
        predicted_price = model.predict(input_df)[0]

    return render_template('index.html', predicted_price=predicted_price)

if __name__ == "__main__":
    app.run(debug=True)