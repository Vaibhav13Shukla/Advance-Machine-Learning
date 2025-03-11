<<<<<<< HEAD
from flask import Flask,request,render_template
=======
from flask import Flask, request, render_template
import logging
>>>>>>> 4df1669 (final commit)
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
<<<<<<< HEAD
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0")        
=======
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Initialize Flask app
application = Flask(__name__)
app = application

# Setup logging for better error tracing
logging.basicConfig(level=logging.DEBUG)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    try:
        if request.method == 'GET':
            return render_template('home.html')
        else:
            # Extract form data
            gender = request.form.get('gender')
            ethnicity = request.form.get('ethnicity')
            parental_level_of_education = request.form.get('parental_level_of_education')
            lunch = request.form.get('lunch')
            test_preparation_course = request.form.get('test_preparation_course')

            # Validate that all required fields are provided
            if not all([gender, ethnicity, parental_level_of_education, lunch, test_preparation_course]):
                raise ValueError("All form fields are required.")

            # Ensure the scores are passed correctly
            try:
                reading_score = float(request.form.get('writing_score', 0))  # Default to 0 if no value
                writing_score = float(request.form.get('reading_score', 0))  # Default to 0 if no value
            except ValueError as e:
                logging.error(f"Invalid score values: {e}")
                return render_template('home.html', results="Invalid score values. Please enter valid numbers.")

            # Create the CustomData object
            data = CustomData(
                gender=gender,
                race_ethnicity=ethnicity,
                parental_level_of_education=parental_level_of_education,
                lunch=lunch,
                test_preparation_course=test_preparation_course,
                reading_score=reading_score,
                writing_score=writing_score
            )

            # Convert the data into DataFrame
            pred_df = data.get_data_as_data_frame()
            logging.debug(f"Prediction DataFrame: {pred_df}")

            # Initialize the prediction pipeline
            predict_pipeline = PredictPipeline()

            # Make the prediction
            results = predict_pipeline.predict(pred_df)
            logging.debug(f"Prediction Results: {results}")

            # Return the results to the HTML template
            return render_template('home.html', results=results[0])

    except Exception as e:
        # Log the error and return a message
        logging.error(f"Error occurred: {str(e)}")
        return render_template('home.html', results="Error occurred during prediction. Please check the logs.")

# Main driver
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
>>>>>>> 4df1669 (final commit)
