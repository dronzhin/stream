import streamlit as st
import json

def save_settings():
    # Сохранение настроек в JSON файл
    settings = {
        "urlollama": st.session_state.urlollama,
        "urlocr": st.session_state.urlocr,
        "model_choice": st.session_state.model_choice,
        "ocr_choice": st.session_state.ocr_choice,
        "prompt": st.session_state.prompt,
        "temp": st.session_state.temp
    }

    return json.dumps(settings, indent=4)

def load_settings_from_file(file):
    # Загрузка настроек из JSON файла
    settings = json.load(file)
    for key, value in settings.items():
        st.session_state[key] = value

def show():
    # Заголовок страницы
    st.title("Настройки")

    if 'urlollama' not in st.session_state:
        st.session_state.urlollama = "http://93.174.229.232:8005/"
    st.session_state.urlollama = st.text_input('URL OLLAMA',value=st.session_state.urlollama)

    if 'urlocr' not in st.session_state:
        st.session_state.urlocr = "http://93.174.229.232:8000/"
    st.session_state.urlocr = st.text_input('URL OCR',value=st.session_state.urlocr)

    # Выбор модели
    options_llm = ["llama3.2-vision", "llama3.2", "deepseek-r1:14b", "qwen2.5:7b"]
    index = 0
    if 'model_choice' in st.session_state:
        index = options_llm.index(st.session_state.model_choice)
    st.session_state.model_choice = st.selectbox("Выберите модель:", options_llm, index=index)

    options_ocr = ["easyocr", "tesseract", "paddleocr", "suryaocr"]
    index = 0
    if 'ocr_choice' in st.session_state:
        index = options_ocr.index(st.session_state.ocr_choice)
    st.session_state.ocr_choice = st.selectbox("Выберите OCR:", options_ocr, index=index)

    # Промпт
    default_prompt = """Ты — медицинский ассистент, специализирующийся на анализе результатов лабораторных исследований. Тебе предоставлен текст, извлеченный из изображения анализов крови с помощью OCR.

    Твоя задача:
    1. Определить основные показатели крови, такие как:

    2. Корректно извлечь числовые значения для каждого показателя.

    3. Сопоставить каждое значение с его единицами измерения (например, г/л, ммоль/л, мг/дл и т. д.)."""

    if 'prompt' not in st.session_state:
        st.session_state.prompt = default_prompt
    st.session_state.prompt = st.text_area("Введите промпт для модели:", height=300, value=st.session_state.prompt)

    # Темп
    if 'temp' not in st.session_state:
        st.session_state.temp = 0.0
    options_temp = [round(i * 0.1, 1) for i in range(11)]  # Генерация значений от 0.0 до 1.0 с шагом 0.1
    new_temp = st.selectbox(
        "Temp:",
        options_temp,
        index=options_temp.index(round(st.session_state.temp, 1)),  # Установка текущего значения
        key="select_temp"
    )
    st.session_state.temp = new_temp

    # Кнопка для скачивания настроек
    json_data = save_settings()
    st.download_button(
        label="Скачать настройки в формате JSON",
        data=json_data,
        file_name='settings.json',
        mime='application/json'
    )

    # Кнопка для загрузки настроек
    uploaded_set = st.file_uploader("Загрузить настройки (JSON)", type="json")
    if uploaded_set is not None:
        load_settings_from_file(uploaded_set)
        st.success("Настройки успешно загружены!")