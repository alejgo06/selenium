from PIL import Image
import urllib.request

def plot_image_from_url(src):
    with urllib.request.urlopen(src) as url:
        s = url.read()
        imageStream = io.BytesIO(s)
        imageFile = Image.open(imageStream)
        display(imageFile)