from PIL import Image, ImageFilter, ImageOps

# blur image
def blur(picture):
    return picture.filter(ImageFilter.BoxBlur(4))
    
# add grayscale
def grayscale(picture):
    return ImageOps.grayscale(picture)

# reflect image
def reflect(picture):
    return ImageOps.mirror(picture)
    
# add contour
def contour(picture):
    return picture.filter(ImageFilter.CONTOUR)
    
# emboss image
def emboss(picture):
    return picture.filter(ImageFilter.EMBOSS)

# sharpen image
def sharpen(picture):
    return picture.filter(ImageFilter.SHARPEN)

# smoothen image
def smoothen(picture):
    return picture.filter(ImageFilter.SMOOTH)
