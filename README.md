# MediGuide: AI-Powered Diagnosis and Treatment Assistant 🏥🚀

Welcome to the MediGuide repository! 🚀

This repository contains the code and resources for MediGuide, an AI-powered healthcare assistant developed as our Senior Design Project (SDP). The application integrates a symptom-based diagnosis chatbot and a deep learning-powered skin disease classifier into a single Flask-based web platform.

## Repository Structure

All components of the project are organized as follows:

- **`datasets/`**: Contains the dataset used for training the skin disease classifier.
  - `skin diseases.v3i.folder/`: Includes subfolders for `train/`, `test/`, and `valid/` datasets with skin disease classes like acne, atopic, and bcc.
  - `README.dataset`, `README.roboflow`: Dataset documentation from the source.
- **`templates/`**: Holds the HTML files used in the Flask web application.
  - `index.html`: Chatbot interface
  - `upload.html`: Image prediction interface
  - `login.html`, `signup.html`: User authentication pages
  - `admin.html`, `home.html`, `layout.html`: Additional layout and navigation templates
- **`static/`**: Contains frontend static files and assets.
  - `images/`: Static UI images
  - `uploads/`: Uploaded images by users
  - `script.js`: JavaScript for UI interactions
  - `styles.css`: Styling for the web pages
- **`app.py`**: The Flask application backend script.
- **`app.db`**: SQLite database for user authentication and session data.
- **`Chatbot.ipynb`**: Jupyter notebook for chatbot model development and training.
- **`Prediction.ipynb`**: Jupyter notebook for skin disease classification and image model evaluation.
- **Model Files**:
  - `best_model.keras`, `CNN_1.h5`, `vgg16.h5`, `skin_disease_model.h5`: Trained deep learning models
  - `svc_model.pkl`, `nn_model.pkl`, `label_encoder.pkl`: Supporting models for chatbot and predictions
- **Flask Backend Logic**:
  - `config.py`, `forms.py`, `models.py`, `sample.py`: Application logic and configurations
- **`requirements.txt`**: List of dependencies required to run the project.
- **`README.md`**: Project overview and instructions (this file).
- **`LICENSE`**: The project license.

## Features

- **Symptom-Based Diagnosis Chatbot**: Predicts disease based on user-entered symptoms and provides recommendations including medications, diets, and precautions.
- **Skin Disease Detection**: Uses deep learning models trained on dermatology datasets to classify skin conditions from user-uploaded images.
- **User Authentication**: Includes login, signup, and admin authentication using Flask and SQLite.
- **Interactive Web Interface**: Built with Flask templates, HTML, CSS, and JavaScript for an intuitive user experience.
- **Multiple ML Models**: Implements neural networks, VGG16, EfficientNet, and SVM for accurate predictions.
- **Modular Design**: Cleanly structured codebase for maintainability and scalability.

## How to Use

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
    ```bash
    git clone https://github.com/VangaLasyaSri/MediGuide_AI-Powered_Diagnosis_and_Treatment_Assisstant.git
    cd MediGuide_AI-Powered_Diagnosis_and_Treatment_Assisstant
    ```

2. **Set Up the Environment**: Navigate to the project directory and create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3. **Install Dependencies**: Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask Application**: Start the Flask app to interact with the model through a web interface:
    ```bash
    python app.py
    ```

5. **Access the Web Interface**: Open your browser and go to `http://localhost:5000` to access the chatbot and image classification features.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. Contributions are always welcome!

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

This project was developed as part of our Senior Design Project (SDP) at VIT-AP University.  
Special thanks to our guide **Prof. Rajesh Duvvuru** for his constant guidance and support.  
We also acknowledge open-source communities and platforms like:  
[Roboflow](https://roboflow.com/) • [Keras](https://keras.io/) • [TensorFlow](https://www.tensorflow.org/) • [Flask](https://flask.palletsprojects.com/) • [Scikit-learn](https://scikit-learn.org/)

Feel free to use this project to explore AI-powered healthcare tools. Happy coding! 🎉
