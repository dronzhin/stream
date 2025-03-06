import requests
import pandas as pd

def ollama_input(url, model_choice, temp, prompt, image = None):
    data = {
        "image": image,
        "model": model_choice,
        "temp": temp,
        "content": prompt
    }

    try:
        response = requests.post(f"{url}process", data=data)
        response.raise_for_status()
        result = response.json()

        # Отображение результата
        if "indicators" in result:
            return pd.DataFrame(result["indicators"])
        else:
            print("Ошибка: В ответе сервера отсутствует ключ 'indicators'.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке запроса: {e}")
        return None