import os.path

from django.shortcuts import render
import json
from cv.settings import STATIC_DIR
from django.http import HttpResponse


# Create your views here.
def home(request, num):
    print(os.path.join(STATIC_DIR, 'content/eurocv{}.json'.format(num)))
    if os.path.isfile(os.path.join(STATIC_DIR, 'content/eurocv{}.json'.format(num))):
        with open(os.path.join(STATIC_DIR, 'content/eurocv{}.json'.format(num)), 'r') as json_file:
            data = json.load(json_file)
        return render(request, 'eurocv.html', {'data': data})
    return HttpResponse("<html><body><h1>CV not found!</h1></body></html>")
