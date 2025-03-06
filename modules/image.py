import base64
from io import BytesIO


# Преобразование PLI
def image_to_base64(image):
        buffered = BytesIO()
        if image.mode in ('RGBA', 'P', 'LA'):
                image = image.convert('RGB')
        image.save(buffered, format="JPEG")  # Сохраняем изображение в буфер как JPEG
        image_bytes = buffered.getvalue()  # Получаем байты
        return base64.b64encode(image_bytes).decode('utf-8')