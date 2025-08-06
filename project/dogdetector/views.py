from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import default_storage
import os

def accueil(request):
    return HttpResponse("Bienvenue sur mon site Django")

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        path = default_storage.save('uploads/' + image.name, image)

        # Ici pour appeler l'ia
        predicted_breed = "Race inconnue (à implémenter)"

        return render(request, 'upload.html', {
            'uploaded': True,
            'breed': predicted_breed,
            'image_url': '/media/' + path
        })
    return render(request, 'upload.html')