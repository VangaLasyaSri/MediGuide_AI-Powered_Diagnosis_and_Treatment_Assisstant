# Chatbot Dataset Description

This folder contains all the structured datasets used by the symptom-based diagnosis chatbot in the MediGuide project.

## Files and Their Purpose

- `symptoms_df.csv`: Main matrix of diseases vs symptoms used for multi-label disease prediction.
- `Symptom-severity.csv`: Maps each symptom to a severity level for risk scoring.
- `precautions_data.csv`: Recommended precautionary measures per disease.
- `medications.csv`: Suggested medicines mapped to predicted diseases.
- `diets.csv`: Dietary advice specific to each condition.
- `workout_df.csv`: Workout and exercise recommendations by disease.
- `description.csv`: Short medical descriptions for each disease.
- `Training.csv`: Cleaned dataset used for training the chatbot’s model.

These files are parsed and used by the chatbot module to make meaningful predictions and offer basic guidance to users based on their symptoms.
