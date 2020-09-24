from django.shortcuts import render
from django.views import generic

# Create your views here.

def index(request):
    return render(request, 'google_data/index.html')


# file upload test
def visualizeLocation(request):
    text = ''
    if request.method == 'POST':
        f = request.FILES.get('location_file')
        text = f.read()
    return render(request, 'google_data/index.html', {'text':text})