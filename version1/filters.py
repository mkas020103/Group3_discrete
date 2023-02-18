from PIL import Image, ImageFilter, ImageOps

# blur image
def blur(picture):
    picture.filter(ImageFilter.BoxBlur(4))
    
# add grayscale
def grayscale(picture):
    ImageOps.grayscale(picture)

# reflect image
def reflect(picture):
    ImageOps.mirror(picture)
    
# add contour
def contour(picture):
    picture.filter(ImageFilter.CONTOUR)
    
# emboss image
def emboss(picture):
    picture.filter(ImageFilter.EMBOSS)

# sharpen image
def sharpen(picture):
    picture.filter(ImageFilter.SHARPEN)

# smoothen image
def smoothen(picture):
    picture.filter(ImageFilter.SMOOTH)
