import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import pickle

# Load datasets
def load_dataset(file_path):
    return pd.read_csv(file_path)

# Preprocess dataset
def preprocess_data(dataset, target_column='prognosis'):
    X = dataset.drop(target_column, axis=1)  # Features
    y = dataset[target_column]  # Target
    le = LabelEncoder()
    y = le.fit_transform(y)  # Encode target labels
    return X, y, le

# Train multiple models
def train_models(X_train, y_train):
    models = {
        'SVC': SVC(kernel='linear'),
        'RandomForest': RandomForestClassifier(n_estimators=100, random_state=42)
    }
    trained_models = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        trained_models[name] = model
    return trained_models

# Evaluate models
def evaluate_models(models, X_test, y_test):
    for name, model in models.items():
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f"{name} Accuracy: {accuracy:.2f}")
        cm = confusion_matrix(y_test, predictions)
        print(f"{name} Confusion Matrix:\n{cm}\n")

# Save model
def save_model(model, filename):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

# Load model
def load_model(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Debugging and Validation
def debug_data_split(y_train, y_test):
    print(f"Train class distribution:\n{pd.Series(y_train).value_counts()}")
    print(f"Test class distribution:\n{pd.Series(y_test).value_counts()}")

def cross_validate_model(model, X, y, cv=5):
    scores = cross_val_score(model, X, y, cv=cv)
    print(f"Cross-validation scores: {scores}")
    print(f"Mean cross-validation accuracy: {scores.mean():.2f}")

# Chatbot interaction
def chatbot_interface(model, symptom_dict, label_encoder, helper_functions):
    print("Welcome to the Disease Prediction Chatbot!")
    print("Enter your symptoms separated by commas (e.g., 'itching, skin_rash'). Type 'exit' to quit.\n")
    
    while True:
        user_input = input("Your symptoms: ").strip().lower()
        if user_input == 'exit':
            print("Goodbye! Stay healthy!")
            break
        
        symptoms = [symptom_dict.get(symptom.strip(), 0) for symptom in user_input.split(",")]
        input_data = [0] * len(symptom_dict)
        for index in symptoms:
            if index:
                input_data[index] = 1
        
        input_df = pd.DataFrame([input_data])
        predicted_disease = label_encoder.inverse_transform(model.predict(input_df))[0]
        print(f"Predicted Disease: {predicted_disease}")
        
        # Retrieve all details for the predicted disease
        desc, precautions, meds, diet, workout = helper_functions(predicted_disease)
        
        # Display additional details
        if input("Do you want to see the description of this disease? (yes/no): ").strip().lower() == 'yes':
            print(f"\nDescription: {desc}")

        if input("Do you want to see the precautions for this disease? (yes/no): ").strip().lower() == 'yes':
            print("Precautions:")
            for p in precautions:
                print(f"- {p}")

        if input("Do you want to see the recommended medications? (yes/no): ").strip().lower() == 'yes':
            print("Medications:", ", ".join(meds))

        if input("Do you want to see the suggested diet? (yes/no): ").strip().lower() == 'yes':
            print("Diet:", ", ".join(diet))

        if input("Do you want to see the workout recommendations? (yes/no): ").strip().lower() == 'yes':
            print("Recommendations:", workout)

        print("\n" + "=" * 40)

# Helper functions for data retrieval
def helper(disease):
    desc = description[description['Disease'] == disease]['Description'].iloc[0]
    precautions_list = precautions.loc[precautions['Disease'] == disease].iloc[:, 1:].values.flatten().tolist()
    meds = medications[medications['Disease'] == disease]['Medication'].tolist()
    diet = diets[diets['Disease'] == disease]['Diet'].tolist()
    workout_plan = workout[workout['disease'] == disease]['workout'].iloc[0]
    return desc, precautions_list, meds, diet, workout_plan

# Main execution
if __name__ == "__main__":
    # File paths
    symptoms_file_path = 'Training.csv'
    precautions_file_path = 'precautions_data.csv'
    description_file_path = 'description.csv'
    medications_file_path = 'medications.csv'
    diets_file_path = 'diets.csv'
    workout_file_path = 'workout_df.csv'
    
    # Load and preprocess data
    symptoms_dataset = load_dataset(symptoms_file_path)
    X, y, label_encoder = preprocess_data(symptoms_dataset)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=20)
    
    # Debug: Check train-test distribution
    print("Debugging Train-Test Split:")
    debug_data_split(y_train, y_test)
    
    # Train models and evaluate
    trained_models = train_models(X_train, y_train)
    evaluate_models(trained_models, X_test, y_test)
    
    # Debug: Cross-validation for models
    print("\nCross-validation for SVC:")
    cross_validate_model(SVC(kernel='linear'), X, y)
    
    print("\nCross-validation for RandomForest:")
    cross_validate_model(RandomForestClassifier(n_estimators=100, random_state=42), X, y)
    
    # Save the best model
    best_model = trained_models['SVC']
    save_model(best_model, 'svc_model.pkl')
    
    save_model(label_encoder,'label_encoder.pkl')

    # Load additional data for chatbot
    precautions = load_dataset(precautions_file_path)
    description = load_dataset(description_file_path)
    medications = load_dataset(medications_file_path)
    diets = load_dataset(diets_file_path)
    workout = load_dataset(workout_file_path)

    # Build symptom dictionary
    symptoms_dict = {symptom: idx for idx, symptom in enumerate(X.columns)}

    # Start chatbot interface
    chatbot_interface(best_model, symptoms_dict, label_encoder, helper)
