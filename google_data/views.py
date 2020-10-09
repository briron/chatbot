from django.shortcuts import render
from django.views import generic
from . import map
from . import android
import base64
from io import BytesIO

# Create your views here.

def index(request):
    text = ''
    return render(request, 'google_data/index.html', {'text':text})


# file upload test
def visualizeTopCountApp(request):
    text = ''
    if request.method == 'POST':
        count = request.POST['count']
        if count is not None and int(count) > 0:
            count = int(count)
        else:
            count = 10
        with request.FILES.get('activity_file') as fp:
            lh = android.AndroidDataHandler(fp=fp)
            service = android.AndroidService(lh)

        tmp = BytesIO()
        fig = service.visualizeTopCountApp(count)
        fig.savefig(tmp, format='png')
        encoded = base64.b64encode(tmp.getvalue()).decode('utf-8')
        text = '<img src=\'data:image/png;base64,{}\'>'.format(encoded)
    return render(request, 'google_data/index.html', {'text':text})

def visualizeLocation(request):
    text = ''
    if request.method == 'POST':
        target = request.POST['target']
        with request.FILES.get('location_file') as fp:
            lh = map.LocationDataHandler(fp=fp)
            service = map.MapService(lh)
        text = service.visualizeNearestLocation(target)._repr_html_()
    return render(request, 'google_data/index.html', {'text':text})