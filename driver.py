from PIL import Image
ASCII = " !\"#$%&'{}*+,-./0123456789:;<=>?@"


def resizeImage(imageFile):
    width, height = imageFile.size
    newWidth =100
    aspectRatio = height / width
    newHeigth = int(newWidth*aspectRatio)
    return imageFile.resize((newWidth,newHeigth))

def grayScale(imageFile):
    return imageFile.convert('L') 


def process(gray):
    pixels = gray.getdata()
    scale_factor = 255 / (len(ASCII) - 1)  # Calculate scale factor accurately
    return ''.join(ASCII[min(int(pixel / scale_factor), len(ASCII) - 1)] for pixel in pixels)

def imgToAscii(imageFile):
    image = resizeImage(imageFile)
    gray = grayScale(image)
    unprocessedImage = process(gray)
    return '\n'.join(unprocessedImage[i:i+100] for i in range(0, len(unprocessedImage),100))


imageFile = 'denzel1.jpg'
im = Image.open(imageFile)

print(im.getbands())
print(im.getbbox())

img = imgToAscii(im)
print(img)
print('asd')


with open("ascii_image.txt", "w") as f:
    f.write(img)  # Write ASCII art to a text file
