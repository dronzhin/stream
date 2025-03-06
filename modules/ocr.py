import requests
from PIL import Image
from modules.image import image_to_base64

url_ocr = "http://93.174.229.232:8000/"

def ocr_input(url, ocr, image):
    payload = {
        "file": image,
        "engine": ocr
    }

    # Make the POST request
    response = requests.post(f"{url}GetOcr", json=payload)

    # Check the response
    if response.status_code == 200:
        result = response.json()["result"]
        return result['text']
    else:
        return response.text

if __name__ == '__main__':
    url_ocr = "http://93.174.229.232:8000/"
    path = 'test_image.jpg'
    image = Image.open(path)
    image64 = image_to_base64(image)

    options_ocr = ["easyocr", "tesseract", "paddleocr", "suryaocr"]
    result = ocr_input(url_ocr, options_ocr[0], image64)
    print(result)

