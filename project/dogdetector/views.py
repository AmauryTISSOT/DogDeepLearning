from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import default_storage
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image
from django.core.files.storage import default_storage
from django.shortcuts import render
import os

MODEL_PATH = ".\model_chien_resnet50_10epochs.h5"
model = load_model(MODEL_PATH)
CLASS_NAMES = [""] #TODO: à compléter
IMG_SIZE = (224,224)

def accueil(request):
    return HttpResponse("Bienvenue sur mon site Django")

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        path = default_storage.save('uploads/' + image.name, image)
        full_path = os.path.join('media', path)

         # Préparation de l'image
        img = keras_image.load_img(full_path, target_size=IMG_SIZE)
        img_array = keras_image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0

        predictions = model.predict(img_array)
        predicted_index = np.argmax(predictions[0])
        predicted_breed = CLASS_NAMES[predicted_index]

        return render(request, 'upload.html', {
            'uploaded': True,
            'breed': predicted_breed,
            'image_url': '/media/' + path
        })
        
    return render(request, 'upload.html')