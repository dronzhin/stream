import streamlit as st
from PIL import Image
from modules.image import image_to_base64
from modules.ollama import ollama_input
from modules.ocr import ocr_input
from src.pages import settings, main, help

# Боковая панель
st.sidebar.title("Меню")
selected_tab = st.sidebar.radio("Выберите вкладку:", ("Главная", "Настройки", "Инструкция"))

if selected_tab == "Главная":
    main.show()
elif selected_tab == "Настройки":
    settings.show()
else:
    help.show()

# if uploaded_file:
#     if model_choice == "llama3.2-vision":
#
#         # Ввод промпта
#         st.write("Пожалуйста, загрузите изображение и введите промпт.")
#         prompt = st.text_area("Введите промпт:", height=100, value=default_prompt)  # Промпт на 3 строки
#
#         # Кнопка для вывода результата
#         if st.button("Вывести результат", key='ollama'):
#
#             if uploaded_file and prompt:
#                 result = ollama_input(
#                     model_choice=model_choice,
#                     temp=0,
#                     prompt=prompt,
#                     image=st.session_state.image64
#                 )
#                 if result is not None:
#                     st.dataframe(result)
#                 else:
#                     st.error("Не удалось получить результат от сервера.")
#             else:
#                 st.warning("Пожалуйста, загрузите изображение и введите промпт.")
#
#
#     elif model_choice in ["llama3.2", "deepseek-r1:14b", "qwen2.5:7b"]:
#
#         # Выбор и обработка
#         ocr_choice = st.selectbox("Выберите OCR:", ["easyocr", "tesseract", "paddleocr", "suryaocr"])
#
#         if uploaded_file:
#             # Создаем форму для OCR и вывода результата
#             if st.button("Распознать через OCR", key='ocr'):
#                 text_input = ocr_input(ocr=ocr_choice, image=st.session_state.image64)
#                 st.session_state.text_input = text_input  # Сохраняем распознанный текст
#
#                 # Отображаем распознанный текст
#                 st.text_area("Распознанный текст:", value=text_input, height=300)
#
#                 # Ввод промпта
#                 st.write("Пожалуйста, введите дополнительный промпт.")
#                 prompt_input = st.text_area("Введите промпт:", height=100, value=default_prompt)
#                 st.session_state.prompt = text_input + ' ' + prompt_input
#
#             # Кнопка для вывода результата
#             if st.session_state.get("text_input") and st.session_state.get("prompt"):
#                 if st.button("Вывести результат", key='result'):
#                     result = ollama_input(
#                         model_choice=model_choice,
#                         temp=0,
#                         prompt=st.session_state.prompt,
#                         image=None
#                     )
#                     if result is not None:
#                         st.dataframe(result)
#                     else:
#                         st.error("Не удалось получить результат от сервера.")
#         else:
#             st.warning("Пожалуйста, загрузите изображение.")





