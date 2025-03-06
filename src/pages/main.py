import streamlit as st
from PIL import Image
from modules.image import image_to_base64
from modules.ollama import ollama_input
from modules.ocr import ocr_input
import pandas as pd

def show():

    # Заголовок страницы
    st.title("Главная")

    # Загрузка изображения
    uploaded_file = st.file_uploader("Загрузите изображение", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        # Отображение загруженного изображения и переводим в base64
        image = Image.open(uploaded_file)
        st.image(image, caption="Загруженное изображение", use_container_width=True)
        st.session_state.image64 = image_to_base64(image)

    if uploaded_file:
        if st.session_state.model_choice == "llama3.2-vision":
            if st.button("Вывести результат", key='ollama'):

                result = ollama_input(
                    url=st.session_state.urlollama,
                    model_choice=st.session_state.model_choice,
                    temp=st.session_state.temp,
                    prompt=st.session_state.prompt,
                    image=st.session_state.image64
                )
                if result is not None:
                    result = pd.DataFrame(result)
                    # Отображение редактируемой таблицы
                    edited_result = st.data_editor(result, key="editable_table")

                    # Кнопка для обработки обновленных данных
                    if st.button("Сохранить изменения"):
                        st.write("Обновленные данные:")
                        st.dataframe(edited_result)
                    st.dataframe(result)
                else:
                    st.error("Не удалось получить результат от сервера.")

        elif st.session_state.model_choice in ["llama3.2", "deepseek-r1:14b", "qwen2.5:7b"]:

            if st.button("Вывести результат", key='ocr'):
                text_input = ocr_input(url=st.session_state.urlocr, ocr=st.session_state.ocr_choice, image=st.session_state.image64)
                st.session_state.prompt_oct = text_input + ' ' + st.session_state.prompt

                result = ollama_input(
                    url=st.session_state.urlollama,
                    model_choice=st.session_state.model_choice,
                    temp=st.session_state.temp,
                    prompt=st.session_state.prompt_oct,
                    image=None
                )
                if result is not None:
                    caption = f'Модель - {st.session_state.model_choice}  \n OCR - {st.session_state.ocr_choice}  \n Temp - {st.session_state.temp}'
                    st.write(caption)
                    st.dataframe(result)
                else:
                    st.error("Не удалось получить результат от сервера.")