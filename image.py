from PIL import Image
from PIL import ImageOps
from PIL import ImageFile



filename = 'temp.png'
img = Image.open(filename)

poster = ImageOps.grayscale(img)

poster.save('poster.png');
