# 🍽️ Food Calorie Estimation System

A deep learning-powered web application that estimates nutritional information from food images using computer vision and machine learning.

## 📋 Overview

This project uses a trained ResNet model to classify food items from images and provide detailed nutritional information including calories, protein, fat, and carbohydrates. The system combines a Django web interface with a TensorFlow/Keras backend for real-time food recognition.

## ✨ Features

- **Image-based Food Recognition**: Upload food images to get instant classification
- **Nutritional Information**: Get detailed nutrition facts including:
  - Calories
  - Protein content
  - Fat content
  - Carbohydrates
- **11 Food Categories**: Trained to recognize multiple food types
- **User-friendly Interface**: Clean web interface for easy interaction
- **Real-time Predictions**: Fast inference using optimized MobileNetV2 model

## 🏗️ Project Structure

```
Calories estimation/
├── BACKEND/
│   └── Food_Calorie_Estimation.ipynb  # Model training notebook
├── DATASET/
│   └── NUTRITIONS.csv                  # Nutritional database
├── FRONTEND/
│   ├── manage.py                       # Django management script
│   ├── best_model_11class.keras        # Trained model (191MB)
│   ├── mobilenetv2_final.h5           # Alternative model
│   ├── 11_class.txt                    # Class labels
│   ├── new_app/                        # Django app
│   │   ├── views.py                    # Main application logic
│   │   ├── urls.py                     # URL routing
│   │   └── models.py                   # Database models
│   ├── new_project/                    # Django project settings
│   │   ├── settings.py                 # Configuration
│   │   └── urls.py                     # Main URL config
│   ├── templates/                      # HTML templates
│   │   ├── index.html
│   │   ├── input.html
│   │   └── output.html
│   ├── static/                         # CSS, JS, images
│   └── assests/                        # Static files
├── README.md                           # This file
└── requirements.txt                    # Python dependencies
```

## 🚀 Installation

### Prerequisites

- Python 3.7 - 3.9 (recommended for TensorFlow compatibility)
- pip package manager
- Virtual environment (recommended)

### Setup Steps

1. **Clone or download the project**
   ```bash
   cd "d:\MOKI Floder\nube matrix\PROJECTS\Calories estimation"
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to the frontend directory**
   ```bash
   cd FRONTEND
   ```

5. **Update file paths in `new_app/views.py`**
   
   Update these paths to match your system:
   ```python
   MODEL_PATH = r"path\to\FRONTEND\best_model_11class.keras"
   NUTRITION_CSV = r"path\to\DATASET\NUTRITIONS.csv"
   TRAIN_TXT = r"path\to\FRONTEND\11_class.txt"
   ```

6. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   
   Open your browser and navigate to: `http://127.0.0.1:8000/`

## 💻 Usage

1. **Home Page**: Navigate to the home page
2. **Upload Image**: Click on the input page and upload a food image
3. **Get Results**: View the predicted food item and nutritional information
4. **Supported Formats**: JPG, JPEG, PNG

## 🧠 Model Information

- **Architecture**: MobileNetV2 (transfer learning)
- **Input Size**: 224x224 RGB images
- **Number of Classes**: 11 food categories
- **Framework**: TensorFlow/Keras
- **Model Size**: ~191 MB (best_model_11class.keras)

### Training

The model was trained using the notebook in `BACKEND/Food_Calorie_Estimation.ipynb`. The training process includes:
- Data preprocessing and augmentation
- Transfer learning from MobileNetV2
- Fine-tuning for food classification
- Validation and testing

## 📊 Dataset

The nutritional information is sourced from `DATASET/NUTRITIONS.csv`, which contains:
- Food names
- Calorie content
- Protein (g)
- Fat (g)
- Carbohydrates (g)

## 🛠️ Technology Stack

- **Backend Framework**: Django 3.0.8
- **Deep Learning**: TensorFlow 2.x, Keras
- **Image Processing**: Pillow (PIL)
- **Data Processing**: NumPy, Pandas
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript

## 🔧 Configuration

### Django Settings

Key settings in `FRONTEND/new_project/settings.py`:
- Debug mode: Enabled (set to False for production)
- Database: SQLite3
- Static files: Configured for development

### Model Configuration

In `FRONTEND/new_app/views.py`:
- Image size: 224x224 pixels
- Preprocessing: RGB conversion, normalization (0-1)
- Prediction: Argmax for class selection

## 📝 API Endpoints

- `/` - Home page
- `/input/` - Image upload page
- `/output/` - Results page (POST only)

## 🐛 Troubleshooting

### Common Issues

1. **Model not loading**
   - Verify MODEL_PATH is correct
   - Ensure the .keras file exists and is not corrupted

2. **Nutrition data not found**
   - Check NUTRITION_CSV path
   - Verify CSV file format matches expected structure

3. **Class names mismatch**
   - Ensure 11_class.txt exists and contains correct class names
   - Verify alphabetical sorting matches training

4. **Import errors**
   - Reinstall requirements: `pip install -r requirements.txt`
   - Check Python version compatibility

## 🔒 Security Notes

⚠️ **For Production Deployment**:
- Change `SECRET_KEY` in settings.py
- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`
- Use environment variables for sensitive data
- Set up proper static file serving
- Use a production-grade database (PostgreSQL, MySQL)
- Implement proper authentication and authorization

## 📈 Future Enhancements

- [ ] Add more food categories
- [ ] Implement user authentication
- [ ] Add meal tracking functionality
- [ ] Create mobile app version
- [ ] Improve model accuracy
- [ ] Add portion size estimation
- [ ] Multi-language support
- [ ] Export nutrition reports

## 👨‍💻 Development

### Running Tests
```bash
cd FRONTEND
python manage.py test
```

### Creating Superuser
```bash
python manage.py createsuperuser
```

### Accessing Admin Panel
Navigate to `http://127.0.0.1:8000/admin/`

## 📄 License

This project is for educational and portfolio purposes.

## 🤝 Contributing

This is a personal portfolio project. Feel free to fork and modify for your own use.

## 📧 Contact

For questions or feedback about this project, please reach out through the repository.

---

**Note**: This is a demonstration project showcasing machine learning and web development skills. The nutritional information provided is for educational purposes and should not replace professional dietary advice.
