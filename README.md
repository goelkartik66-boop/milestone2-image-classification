# Milestone 2 - Image Classification with Flask

## Project Overview
This project implements an image classification model that distinguishes between two shape types (circles and squares) using machine learning and deploys it as a local Flask API.

## Project Structure
milestone 2/
├── data/
│ └── synthetic_images/
│ ├── circle/
│ └── square/
├── src/
│ ├── app.py
│ ├── train_model.py
│ ├── generate_dataset.py
│ ├── image_model.pkl
│ └── requirements.txt
├── docs/
│ ├── project_report.docx
│ └── project_presentation.pptx
└── README.md

## How to Run

### 1. Generate Dataset
cd C:\milestone 2\src
python generate_dataset.py
This creates synthetic images in `data/synthetic_images/`.

### 2. Train the Model
python train_model.py
This trains the classifier and saves it as `image_model.pkl`.

### 3. Run the Flask API
python app.py
The API will start at `http://127.0.0.1:5000`.

### 4. Test the API
Create a new PowerShell window and run:
python test_api.py

## API Endpoint

**POST** `/predict`
- **Description:** Predicts the class of an uploaded image.
- **Input:** Image file (circle or square).
- **Output:** JSON with prediction.

**Example Response:**
{"prediction": "circle"}

## Technologies Used
- Python 3.10
- Flask
- scikit-learn
- Pillow (PIL)
- NumPy

## Author
Kartik - A25ARIU0019
Keshav - A25ARIU0021

## Date
November 22, 2025

