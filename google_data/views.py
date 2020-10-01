from django.shortcuts import render
from django.views import generic
from . import map

# Create your views here.

def index(request):
    return render(request, 'google_data/index.html')


# file upload test
def visualizeLocation(request):
    text = ''
    if request.method == 'POST':
        target = request.POST['target']
        with request.FILES.get('location_file') as fp:
            lh = map.LocationDataHandler(fp=fp)
            service = map.MapService(lh)
        text = service.visualizeNearestLocation(target)._repr_html_()
    return render(request, 'google_data/index.html', {'text':text})