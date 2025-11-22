import os
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

data = []
labels = []

base_dir = "../data/synthetic_images"  # adjust as needed if running from src

for label in ["circle", "square"]:
    for file in os.listdir(os.path.join(base_dir, label)):
        img_path = os.path.join(base_dir, label, file)
        img = np.array(Image.open(img_path).resize((32, 32))).flatten()
        data.append(img)
        labels.append(label)

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.3, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))
pickle.dump(model, open("image_model.pkl", "wb"))
