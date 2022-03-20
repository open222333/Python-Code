from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open("ch17/fortest.jpeg"))
print(type(text), "   ", text)
