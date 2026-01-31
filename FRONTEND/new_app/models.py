from django.db import models
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from keras.models import load_model
import numpy as np
import pickle
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import json
from PIL import Image


from tensorflow.keras.models import load_model

#cnn = load_model(r'C:\Users\prasu\Music\DEEP_FAKE\FRONTEND\vgg.h5')
model = load_model(r'C:\Users\User\Music\SKIN_CANCER\FRONTEND\Densenet_Skin_Cancer.h5')

def predict(img,algo): 
	file = Image.open(img)
	img = file.convert('RGB')
	img_bgr= img.resize((126, 126))
	img_bgr = np.array(img_bgr)
	
	#res = cv2.resize(img,(48,48), interpolation = cv2.INTER_CUBIC)
	res = img_bgr.reshape([-1,126, 126,3])
	#res = img_array.reshape(-1, 48, 48, 1)
	print(res.shape)
	if algo=='model':
		y_pred=model.predict(res)
		return y_pred[0]
	else:
		y_pred=model.predict(res)
		return y_pred[0]