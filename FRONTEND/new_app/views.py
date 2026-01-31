# views.py
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from PIL import Image
import numpy as np
import pandas as pd
import os

from tensorflow.keras.models import load_model

# --------------------------------------------------
# CONFIGURATION (CHANGE PATHS IF NEEDED)
# --------------------------------------------------
MODEL_PATH = r"C:\Users\dinnu\Music\Calories estimation\FRONTEND\best_model_11class.keras"
NUTRITION_CSV = r"C:\Users\dinnu\Music\Calories estimation\DATASET\NUTRITIONS.csv"
TRAIN_TXT = r"C:\Users\dinnu\Music\Calories estimation\FRONTEND\11_class.txt"

IMAGE_SIZE = (224, 224)

# --------------------------------------------------
# HELPERS
# --------------------------------------------------
def canonicalize_name(name):
    return (
        str(name)
        .strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
    )

# --------------------------------------------------
# LOAD CLASS NAMES FROM train.txt (CRITICAL FIX)
# --------------------------------------------------
def load_class_names_from_train_txt():
    if not os.path.exists(TRAIN_TXT):
        raise RuntimeError("train.txt not found")

    class_set = set()

    with open(TRAIN_TXT, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # apple_pie/1005649 -> apple_pie
            class_name = line.split("/")[0]
            class_set.add(class_name)

    # IMPORTANT: alphabetical sort (Keras behavior)
    class_names = sorted(class_set)

    if len(class_names) == 0:
        raise RuntimeError("No classes found in train.txt")

    return np.array(class_names)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
model = None
try:
    model = load_model(MODEL_PATH)
except Exception as e:
    print("⚠️ Model loading failed:", e)

# --------------------------------------------------
# LOAD NUTRITION DATA
# --------------------------------------------------
nutrition_df = pd.read_csv(NUTRITION_CSV)
nutrition_df["name_canonical"] = nutrition_df["name"].apply(canonicalize_name)

# --------------------------------------------------
# LOAD CLASS NAMES (FROM train.txt)
# --------------------------------------------------
class_names = load_class_names_from_train_txt()

# --------------------------------------------------
# IMAGE UTILITIES
# --------------------------------------------------
def validate_image(img_file):
    try:
        Image.open(img_file).verify()
        img_file.seek(0)
    except Exception:
        raise ValidationError("Invalid image file")

def preprocess_image(image_file):
    img = Image.open(image_file).convert("RGB")
    img = img.resize(IMAGE_SIZE)
    arr = np.array(img, dtype=np.float32) / 255.0
    arr = np.expand_dims(arr, axis=0)
    return arr

# --------------------------------------------------
# VIEWS
# --------------------------------------------------
def home(request):
    return render(request, "index.html")

def input(request):
    return render(request, "input.html")

def output(request):
    if request.method != "POST":
        return HttpResponse("Invalid request method")

    if "file" not in request.FILES:
        return HttpResponse("No image uploaded")

    if model is None:
        return HttpResponse("Model not loaded on server")

    img = request.FILES["file"]

    try:
        validate_image(img)
        processed_img = preprocess_image(img)
        preds = model.predict(processed_img)
    except Exception as e:
        return HttpResponse(f"Prediction error: {e}")

    idx = int(np.argmax(preds, axis=1)[0])

    if idx >= len(class_names):
        return HttpResponse("Prediction index out of range")

    predicted_canonical = class_names[idx]

    # Display name
    food_display = predicted_canonical.replace("_", " ").title()

    # Nutrition lookup
    row = nutrition_df[nutrition_df["name_canonical"] == predicted_canonical]

    if not row.empty:
        row = row.iloc[0]
        calories = row.get("calories", "N/A")
        protein = row.get("protein", "N/A")
        fat = row.get("fat", "N/A")
        carbohydrates = row.get("carbohydrates", "N/A")
    else:
        calories = protein = fat = carbohydrates = "N/A"

    context = {
        "food_item": food_display,
        "calories": calories,
        "protein": protein,
        "fat": fat,
        "carbohydrates": carbohydrates,
        "predicted_class": predicted_canonical,
    }

    return render(request, "output.html", context)
