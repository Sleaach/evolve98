import cv2
import time
from PIL import Image

def asci():
 ASCII_CHARS = '@%#*+=-:. ₺$£1u[̉ €];&¾~|{}0ß»«¢“”µ×·ª?^<>!'

 def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / float(width)
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image
 
 def grayify(image):
    grayscale_image = image.convert('L')
    return grayscale_image
 
 def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        if 0 <= pixel_value < 256: 
            # Check the length of ASCII_CHARS list and limit the index
            index = min(pixel_value // 25, len(ASCII_CHARS) - 1)
            ascii_str += ASCII_CHARS[index]
        else:
            ascii_str += ' '  # Use space character if pixel value is out of range
    return ascii_str
 
 def video_to_ascii(video_path):
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = resize_image(image)
        image = grayify(image)
        ascii_str = pixels_to_ascii(image)
        ascii_str = '\n'.join([ascii_str[i:i+image.width] for i in range(0, len(ascii_str), image.width)])
        print(ascii_str)
        time.sleep(0.1)
    cap.release()

  
 video_path = input("Video: ")
 video_to_ascii(video_path)



