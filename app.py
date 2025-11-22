from flask import Flask, request, jsonify
import pickle
import numpy as np
from PIL import Image

app = Flask(__name__)
model = pickle.load(open("image_model.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    img = np.array(Image.open(file).resize((32, 32))).flatten().reshape(1, -1)
    pred = model.predict(img)
    return jsonify({'prediction': pred[0]})

if __name__ == '__main__':
    app.run(debug=True)
