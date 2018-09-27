from django.shortcuts import render
from django.shortcuts import HttpResponse
import re
import base64


def index(request):

    return render(request, 'take_snapshot.html')


def save_screenshot(request):

    dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
    image_data = request.POST['imagedata']
    image_data = dataUrlPattern.match(image_data).group(2)
    image_data = image_data.encode()
    image_data = base64.b64decode(image_data)

    with open(r'Snapshot/static/images/screenshot.jpg', 'wb') as f:
        f.write(image_data)

    return render(request, 'display.html')