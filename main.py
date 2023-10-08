# 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
import tkinter as tk
import time
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import openai
import webbrowser
import pyttsx3
from PIL import Image, ImageTk
import os
import requests
import threading
from datetime import datetime

import dictionary
from updates import updatemenu
from settings import (api_key, font_save, voice_save, lang_save, theme_save, gpt_mod, gpt_model, gpt_parameters,
                      save_folder, ask_save, save_or_no)



# настройки чата
api_key = api_key
engine = pyttsx3.init()
font_save = font_save
voice_save = voice_save
lang_save = lang_save
theme_save = theme_save
gpt_mod = gpt_mod
gpt_model = gpt_model
gpt_parameters = gpt_parameters
save_folder = save_folder
ask_save = ask_save
save_or_no = save_or_no
eng = [
       'Settings',
       'Clear conversations',
       'ChatGPT settings',
       'Interface',
       'Theme',
       'System',
       'Light',
       'Dark',
       'API key',
       'Set API key',
       'Language',
       'Voiceover',
       'Model',
       'Token',
       'Temperature',
       'Confirmation',
       'Are you sure you want to go to the site? After confirmation, you will be redirected to the official openai website.'
       ]
rus = [
        'Настройки',
        'Очистить диалог',
        'Настройки ChatGPT',
        'Интерфейс',
        'Тема',
        'Системная',
        'Светлая',
        'Темная',
        'API ключ',
        'Установить API ключ',
        'Язык',
        'Озвучка',
        'Модель',
        'Токен',
        'Температура',
        'Подтверждение',
        'Вы уверены, что хотите перейти на сайт? После подтверждения вы будете перенаправлены на официальный сайт OpenAI.'
       ]
esp = [
        'Configuración',
        'Borrar conversaciones',
        'Configuración de ChatGPT',
        'Interfaz',
        'Tema',
        'Sistema',
        'Claro',
        'Oscuro',
        'Clave de API',
        'Establecer clave de API',
        'Idioma',
        'Locución',
        'Modelo',
        'Token',
        'Temperatura',
        'Confirmación',
        '¿Estás seguro de que deseas ir al sitio web? Después de la confirmación, serás redirigido al sitio web oficial de OpenAI.'
        ]
deu = [
        'Einstellungen',
        'Konversationen löschen',
        'ChatGPT-Einstellungen',
        'Benutzeroberfläche',
        'Thema',
        'System',
        'Hell',
        'Dunkel',
        'API-Schlüssel',
        'API-Schlüssel festlegen',
        'Sprache',
        'Vertonung',
        'Modell',
        'Token',
        'Temperatur',
        'Bestätigung',
        'Sind Sie sicher, dass Sie zur Website gehen möchten? Nach der Bestätigung werden Sie zur offiziellen OpenAI-Website weitergeleitet.'
        ]
tur = [
        'Ayarlar',
        'Konuşmaları temizle',
        'ChatGPT ayarları',
        'Arayüz',
        'Tema',
        'Sistem',
        'Açık',
        'Karanlık',
        'API anahtarı',
        'API anahtarını ayarla',
        'Dil',
        'Seslendirme',
        'Model',
        'Jeton',
        'Sıcaklık',
        'Onay',
        'Siteye gitmek istediğinizden emin misiniz? Onaylandıktan sonra resmi OpenAI web sitesine yönlendirileceksiniz.'
        ]
ukr = [
        'Налаштування',
        'Очистити діалог',
        'Налаштування ChatGPT',
        'Інтерфейс',
        'Тема',
        'Системна',
        'Світла',
        'Темна',
        'API-ключ',
        'Встановити API-ключ',
        'Мова',
        'Озвучення',
        'Модель',
        'Токен',
        'Температура',
        'Підтвердження',
        'Ви впевнені, що бажаєте перейти на сайт? Після підтвердження ви будете перенаправлені на офіційний сайт OpenAI.'
        ]

if lang_save[0] == 'English':
    main_lang = eng
elif lang_save[0] == 'Russian':
    main_lang = rus
elif lang_save[0] == 'Spanish':
    main_lang = esp
elif lang_save[0] == 'German':
    main_lang = deu
elif lang_save[0] == 'Turkish':
    main_lang = tur
elif lang_save[0] == 'Ukrainian':
    main_lang = ukr




# Пример использования OpenAI для генерации текста
def generate_text(prompt, *args):
    response = openai.ChatCompletion.create(
        model=gpt_model[0],
        max_tokens=gpt_parameters[0],
        temperature=gpt_parameters[1],
        top_p=gpt_parameters[2],
        frequency_penalty=gpt_parameters[3],
        presence_penalty=gpt_parameters[4],
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    # Получение сгенерированного текста из Chat Completion
    completion_text = response.choices[0].message.content.strip()

    return completion_text

def speak(text):
    engine.say(text)
    engine.runAndWait()


def send_message():
    message = input_entry.get().strip()
    print(message)
    if message:
        response = generate_text("User: " + message + "\n")
        output_text.configure(state="normal")
        if lang_save[0] == 'English':
            output_text.insert("end", "Your: " + message + "\n", "bold")
            output_text.insert("end", "Chat: " + response + "\n")
        elif lang_save[0] == 'Russian':
            output_text.insert("end", "Ты: " + message + "\n", "bold")
            output_text.insert("end", "Чат: " + response + "\n")
        elif lang_save[0] == 'Spanish':
            output_text.insert("end", "Tuyo: " + message + "\n", "bold")
            output_text.insert("end", "Chat: " + response + "\n")
        elif lang_save[0] == 'German':
            output_text.insert("end", "Deine Nachricht: " + message + "\n", "bold")
            output_text.insert("end", "Chat: " + response + "\n")
        elif lang_save[0] == 'Turkish':
            output_text.insert("end", "Senin: " + message + "\n", "bold")
            output_text.insert("end", "Chat: " + response + "\n")
        elif lang_save[0] == 'Ukrainian':
            output_text.insert("end", "Ти: " + message + "\n", "bold")
            output_text.insert("end", "Чат: " + response + "\n")

        if voice_save[0] == 'On':
            speak(response)
        elif voice_save[0] == 'Off':
            engine.stop()

        output_text.configure(state="disabled")
        input_entry.delete(0, "end")
        input_entry.focus()
        print(response)






#  Создание окна
app = ctk.CTk()
app.title("ChatGPT")
app.iconbitmap('chatgpt.ico')
app.minsize(800, 600)



def app_theme():
    if theme_save[0] == 'Light':
        ctk.set_appearance_mode('Light')
        output_text.configure(fg_color='#f7f7f8', text_color='black')
        app.configure(fg_color='#ffffff')
        frame.configure(fg_color='#ffffff')
        input_entry.configure(fg_color='#ffffff', text_color='black')
    elif theme_save[0] == 'Dark':
        ctk.set_appearance_mode("dark")
        output_text.configure(fg_color='#454553', text_color='#d2cab4')
        app.configure(fg_color='#363640')
        frame.configure(fg_color='#363640')
        input_entry.configure(fg_color='#363640', text_color='#d2cab4')



# Создание рамки для виджетов ввода и вывода
frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True, padx=1, pady=1)

# Создание виджета Text для вывода ответовS
output_text = ctk.CTkTextbox(frame, width=80, height=20, state="disabled", activate_scrollbars=False)
output_text.configure(font=(font_save[0], font_save[1]))
output_text.pack(side="left", fill="both", expand=True, padx=10, pady=10)

scrollbar = ctk.CTkScrollbar(frame)
scrollbar.pack(side="right", fill="y")

scrollbar.configure(command=output_text.yview)
output_text.configure(yscrollcommand=scrollbar.set)




def settings():


    def on_closing():
        window.grab_release()
        window.destroy()
        app.focus_set()
        app.grab_set()


    window = ctk.CTkToplevel(app)
    window.title('Settings')
    window.iconbitmap('chatgpt.ico')
    window.geometry('675x375')
    window.resizable(False, False)
    window.iconbitmap('chatgpt.ico')
    window.protocol("WM_DELETE_WINDOW", on_closing)

    # Ограничиваем перемещение окна только внутри главного окна
    window.transient()  # Делаем второе окно зависимым от главного
    window.grab_set()  # Захватываем фокус



    frame_settings = ctk.CTkFrame(window, width=425, height=350)
    frame_settings.place(relx=0.328, rely=0.5, anchor=tk.CENTER)
    frame_interface = ctk.CTkFrame(window, width=225, height=350)
    frame_interface.place(relx=0.82, rely=0.5, anchor=tk.CENTER)
    chat_settings = ctk.CTkLabel(frame_settings, text='ChatGPT settings', font=("Arial", 24))
    chat_settings.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    interface = ctk.CTkLabel(frame_interface, text='Interface', font=("Arial", 24))
    interface.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    quest_image = ctk.CTkImage(light_image=Image.open("images\quest.ico"),
                               dark_image=Image.open("images\quest.ico"),
                               size=(20, 20))
    quest = ctk.CTkButton(frame_settings,
                          text='',
                          width=1, height=1,
                          image=quest_image,
                          command=updatemenu)
    quest.place(relx=0.95, rely=0.935, anchor=tk.CENTER)

    def api():
        openai.api_key = api_entry.get()
        if openai.api_key.startswith('sk-') and len(openai.api_key) == 51:
            api_btn.configure(fg_color='green')
            def on_enter(event):
                api_btn.configure(fg_color='green')
            def on_leave(event):
                api_btn.configure(fg_color='green')
            def on_click(event):
                api_btn.configure(fg_color='green')
            api_btn.bind('<Enter>', on_enter)
            api_btn.bind('<Leave>', on_leave)
            api_btn.bind('<Button-1>', on_click)
            print(f'Api key: {openai.api_key}')

        else:
            api_btn.configure(fg_color='red')
            def on_enter(event):
                api_btn.configure(fg_color='red')
            def on_leave(event):
                api_btn.configure(fg_color='red')
            def on_click(event):
                api_btn.configure(fg_color='red')
            api_btn.bind('<Enter>', on_enter)
            api_btn.bind('<Leave>', on_leave)
            api_btn.bind('<Button-1>', on_click)
            print('Error')
        with open('settings.py', 'w') as configfile:
            configfile.write(f"import openai\n")
            configfile.write(f"\n")
            if openai.api_key.startswith('sk-') and len(openai.api_key) == 51:
                configfile.write(f"openai.api_key = '{openai.api_key}'\n")
            else:
                configfile.write(f"openai.api_key = ''\n")
            configfile.write(f"api_key = openai.api_key\n")
            configfile.write(f"font_save = {font_save}\n")
            configfile.write(f"voice_save = {voice_save}\n")
            configfile.write(f"lang_save = {lang_save}\n")
            configfile.write(f"theme_save = {theme_save}\n")
            configfile.write(f"gpt_mod = {gpt_mod}\n")
            configfile.write(f"gpt_model = {gpt_model}\n")
            configfile.write(f"gpt_parameters = {gpt_parameters}\n")
            configfile.write(f"save_folder = '{save_folder}'\n")
            configfile.write(f"ask_save = True\n")
            configfile.write(f"save_or_no = True\n")


    def insert_api():
        # Получаем текст из буфера обмена
        clipboard_text = app.clipboard_get()
        # Вставляем текст в Entry виджет
        api_entry.insert(tk.END, clipboard_text)

    paste_image = ctk.CTkImage(light_image=Image.open("images\pasted.png"),
                              dark_image=Image.open("images\pasted.png"),
                              size=(20, 20))
    api_lab = ctk.CTkLabel(frame_settings, text='API key')
    api_entry = ctk.CTkEntry(frame_settings, width=370)
    api_entry.insert(0, openai.api_key)
    api_btn = ctk.CTkButton(frame_settings, text='Set API key', command=api)
    if openai.api_key.startswith('sk-') and len(openai.api_key) == 51:
        api_btn.configure(fg_color='green')
    else:
        api_btn.configure(fg_color='red')
    api_paste = ctk.CTkButton(frame_settings, text='', width=1, image=paste_image, command=insert_api)

    api_lab.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    api_entry.place(relx=0.45, rely=0.3, anchor=tk.CENTER)
    api_btn.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    api_paste.place(relx=0.935, rely=0.3, anchor=tk.CENTER)


    def print_selected_option(*args):
        if selected_option.get() == 'Light':
            del theme_save[0]
            theme_save.append('Light')
            print(selected_option.get())
            ctk.set_appearance_mode('Light')
            output_text.configure(fg_color='#f7f7f8', text_color='black')
            app.configure(fg_color='#ffffff')
            frame.configure(fg_color='#ffffff')
            input_entry.configure(fg_color='#ffffff', text_color='black')
            window.configure(fg_color='#ffffff')
            api_entry.configure(fg_color='#ffffff', text_color='black')
            api_lab.configure(fg_color='#f7f7f8', text_color='black')
            theme_label.configure(fg_color='#f7f7f8', text_color='black')
            chat_settings.configure(fg_color='#f7f7f8', text_color='black')
            interface.configure(fg_color='#f7f7f8', text_color='black')
            frame_settings.configure(fg_color='#f7f7f8')
            frame_interface.configure(fg_color='#f7f7f8')
            lang_lab.configure(fg_color='#f7f7f8', text_color='black')
            voice_lab.configure(fg_color='#f7f7f8', text_color='black')
            model_lab.configure(fg_color='#f7f7f8', text_color='black')
            token_lab.configure(fg_color='#f7f7f8', text_color='black')
            token_counter.configure(fg_color='#f7f7f8', text_color='black')
            temp_lab.configure(fg_color='#f7f7f8', text_color='black')
            temp_counter.configure(fg_color='#f7f7f8', text_color='black')
        elif selected_option.get() == 'Dark':
            del theme_save[0]
            theme_save.append('Dark')
            print(selected_option.get())
            ctk.set_appearance_mode("dark")
            output_text.configure(fg_color='#454553', text_color='#d2cab4')
            app.configure(fg_color='#363640')
            frame.configure(fg_color='#363640')
            input_entry.configure(fg_color='#363640', text_color='#d2cab4')
            window.configure(fg_color='#363640')
            api_entry.configure(fg_color='#363640', text_color='#d2cab4')
            api_lab.configure(fg_color='#454553', text_color='#d2cab4')
            theme_label.configure(fg_color='#454553', text_color='#d2cab4')
            chat_settings.configure(fg_color='#454553', text_color='#d2cab4')
            interface.configure(fg_color='#454553', text_color='#d2cab4')
            frame_settings.configure(fg_color='#454553')
            frame_interface.configure(fg_color='#454553')
            lang_lab.configure(fg_color='#454553', text_color='#d2cab4')
            voice_lab.configure(fg_color='#454553', text_color='#d2cab4')
            model_lab.configure(fg_color='#454553', text_color='#d2cab4')
            token_lab.configure(fg_color='#454553', text_color='#d2cab4')
            token_counter.configure(fg_color='#454553', text_color='#d2cab4')
            temp_lab.configure(fg_color='#454553', text_color='#d2cab4')
            temp_counter.configure(fg_color='#454553', text_color='#d2cab4')
        with open('settings.py', 'w') as configfile:
            configfile.write(f"import openai\n")
            configfile.write(f"\n")
            if openai.api_key.startswith('sk-') and len(openai.api_key) == 51:
                configfile.write(f"openai.api_key = '{openai.api_key}'\n")
            else:
                configfile.write(f"openai.api_key = ''\n")
            configfile.write(f"api_key = openai.api_key\n")
            configfile.write(f"font_save = {font_save}\n")
            configfile.write(f"voice_save = {voice_save}\n")
            configfile.write(f"lang_save = {lang_save}\n")
            configfile.write(f"theme_save = {theme_save}\n")
            configfile.write(f"gpt_mod = {gpt_mod}\n")
            configfile.write(f"gpt_model = {gpt_model}\n")
            configfile.write(f"gpt_parameters = {gpt_parameters}\n")
            configfile.write(f"save_folder = '{save_folder}'\n")
            configfile.write(f"ask_save = True\n")
            configfile.write(f"save_or_no = True\n")


    themes = ['Light', 'Dark']
    selected_option = ctk.StringVar(value=theme_save[0])
    selected_option.trace_add("write", print_selected_option)
    theme_label = ctk.CTkLabel(frame_interface, text='Theme', font=("Arial", 16))
    theme_option_menu = ctk.CTkOptionMenu(master=frame_interface, values=themes, variable=selected_option, width=100)

    theme_label.place(relx=0.115, rely=0.3, anchor=tk.CENTER)
    theme_option_menu.place(relx=0.75, rely=0.3, anchor=tk.CENTER)


    def languages(*args):

        if selected_lang.get() == 'English':
            del lang_save[0]
            lang_save.append('English')
            chat_settings.configure(text=eng[2])
            interface.configure(text=eng[3])
            api_lab.configure(text=eng[8])
            api_btn.configure(text=eng[9])
            theme_label.configure(text=eng[4])
            lang_lab.configure(text=eng[10])
            voice_lab.configure(text=eng[11])
            model_lab.configure(text=eng[12])
            token_lab.configure(text=eng[13])
            temp_lab.configure(text=eng[14])
            theme_label.place(relx=0.115, rely=0.3, anchor=tk.CENTER)
            lang_lab.place(relx=0.175, rely=0.4, anchor=tk.CENTER)
            voice_lab.place(relx=0.17, rely=0.5, anchor=tk.CENTER)
        elif selected_lang.get() == 'Русский':
            del lang_save[0]
            lang_save.append('Russian')
            chat_settings.configure(text=rus[2])
            interface.configure(text=rus[3])
            api_lab.configure(text=rus[8])
            api_btn.configure(text=rus[9])
            theme_label.configure(text=rus[4])
            lang_lab.configure(text=rus[10])
            voice_lab.configure(text=rus[11])
            model_lab.configure(text=rus[12])
            token_lab.configure(text=rus[13])
            temp_lab.configure(text=rus[14])
            theme_label.place(relx=0.1, rely=0.3, anchor=tk.CENTER)
            lang_lab.place(relx=0.1, rely=0.4, anchor=tk.CENTER)
            voice_lab.place(relx=0.14, rely=0.5, anchor=tk.CENTER)
        elif selected_lang.get() == 'Español':
            del lang_save[0]
            lang_save.append('Spanish')
            chat_settings.configure(text=esp[2])
            interface.configure(text=esp[3])
            api_lab.configure(text=esp[8])
            api_btn.configure(text=esp[9])
            theme_label.configure(text=esp[4])
            lang_lab.configure(text=esp[10])
            voice_lab.configure(text=esp[11])
            model_lab.configure(text=esp[12])
            token_lab.configure(text=esp[13])
            temp_lab.configure(text=esp[14])
            theme_label.place(relx=0.1, rely=0.3, anchor=tk.CENTER)
            lang_lab.place(relx=0.125, rely=0.4, anchor=tk.CENTER)
            voice_lab.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
        elif selected_lang.get() == 'Deutsch':
            del lang_save[0]
            lang_save.append('German')
            chat_settings.configure(text=deu[2])
            interface.configure(text=deu[3])
            api_lab.configure(text=deu[8])
            api_btn.configure(text=deu[9])
            theme_label.configure(text=deu[4])
            lang_lab.configure(text=deu[10])
            voice_lab.configure(text=deu[11])
            model_lab.configure(text=deu[12])
            token_lab.configure(text=deu[13])
            temp_lab.configure(text=deu[14])
            theme_label.place(relx=0.115, rely=0.3, anchor=tk.CENTER)
            lang_lab.place(relx=0.135, rely=0.4, anchor=tk.CENTER)
            voice_lab.place(relx=0.17, rely=0.5, anchor=tk.CENTER)
        elif selected_lang.get() == 'Türkçe':
            del lang_save[0]
            lang_save.append('Turkish')
            chat_settings.configure(text=tur[2])
            interface.configure(text=tur[3])
            api_lab.configure(text=tur[8])
            api_btn.configure(text=tur[9])
            theme_label.configure(text=tur[4])
            lang_lab.configure(text=tur[10])
            voice_lab.configure(text=tur[11])
            model_lab.configure(text=tur[12])
            token_lab.configure(text=tur[13])
            temp_lab.configure(text=tur[14])
            theme_label.place(relx=0.115, rely=0.3, anchor=tk.CENTER)
            lang_lab.place(relx=0.078, rely=0.4, anchor=tk.CENTER)
            voice_lab.place(relx=0.225, rely=0.5, anchor=tk.CENTER)

        elif selected_lang.get() == 'Український':
            del lang_save[0]
            lang_save.append('Ukrainian')
            chat_settings.configure(text=ukr[2])
            interface.configure(text=ukr[3])
            api_lab.configure(text=ukr[8])
            api_btn.configure(text=ukr[9])
            theme_label.configure(text=ukr[4])
            lang_lab.configure(text=ukr[10])
            voice_lab.configure(text=ukr[11])
            model_lab.configure(text=ukr[12])
            token_lab.configure(text=ukr[13])
            temp_lab.configure(text=ukr[14])
            theme_label.place(relx=0.1, rely=0.3, anchor=tk.CENTER)
            lang_lab.place(relx=0.1, rely=0.4, anchor=tk.CENTER)
            voice_lab.place(relx=0.18, rely=0.5, anchor=tk.CENTER)
        print(f'Language: {selected_lang.get()}')
        with open('settings.py', 'w') as configfile:
            configfile.write(f"import openai\n")
            configfile.write(f"\n")
            if openai.api_key.startswith('sk-') and len(openai.api_key) == 51:
                configfile.write(f"openai.api_key = '{openai.api_key}'\n")
            else:
                configfile.write(f"openai.api_key = ''\n")
            configfile.write(f"api_key = openai.api_key\n")
            configfile.write(f"font_save = {font_save}\n")
            configfile.write(f"voice_save = {voice_save}\n")
            configfile.write(f"lang_save = {lang_save}\n")
            configfile.write(f"theme_save = {theme_save}\n")
            configfile.write(f"gpt_mod = {gpt_mod}\n")
            configfile.write(f"gpt_model = {gpt_model}\n")
            configfile.write(f"gpt_parameters = {gpt_parameters}\n")
            configfile.write(f"save_folder = '{save_folder}'\n")
            configfile.write(f"ask_save = True\n")
            configfile.write(f"save_or_no = True\n")
            app.update()
            window.update()



    lang = ['Deutsch', 'English', 'Español', 'Русский', 'Türkçe', 'Український']
    selected_lang = ctk.StringVar(value=lang_save[0])
    selected_lang.trace_add("write", languages)
    lang_option = ctk.CTkOptionMenu(master=frame_interface, values=lang, variable=selected_lang, width=100)
    lang_option.place(relx=0.75, rely=0.4, anchor=tk.CENTER)

    lang_lab = ctk.CTkLabel(frame_interface, text=eng[10], font=("Arial", 16))
    lang_lab.place(relx=0.175, rely=0.4, anchor=tk.CENTER)


    def on_voice_selected(*args):
        # Выключение озвучки
        if voice_var.get() == "Off":
            del voice_save[0]
            voice_save.append('Off')
        # Выбор мужской озвучки
        elif voice_var.get() == "On":
            del voice_save[0]
            voice_save.append('On')
        with open('settings.py', 'w') as configfile:
            configfile.write(f"import openai\n")
            configfile.write(f"\n")
            if openai.api_key.startswith('sk-') and len(openai.api_key) == 51:
                configfile.write(f"openai.api_key = '{openai.api_key}'\n")
            else:
                configfile.write(f"openai.api_key = ''\n")
            configfile.write(f"api_key = openai.api_key\n")
            configfile.write(f"font_save = {font_save}\n")
            configfile.write(f"voice_save = {voice_save}\n")
            configfile.write(f"lang_save = {lang_save}\n")
            configfile.write(f"theme_save = {theme_save}\n")
            configfile.write(f"gpt_mod = {gpt_mod}\n")
            configfile.write(f"gpt_model = {gpt_model}\n")
            configfile.write(f"gpt_parameters = {gpt_parameters}\n")
            configfile.write(f"save_folder = '{save_folder}'\n")
            configfile.write(f"ask_save = True\n")
            configfile.write(f"save_or_no = True\n")
        print(f'Voice: {voice_var.get()}')


    voice_var = ctk.StringVar(value=voice_save[0])
    voice_switch = ctk.CTkSwitch(master=frame_interface, text="", command=on_voice_selected,
                                       variable=voice_var, onvalue="On", offvalue="Off", width=0, state="disabled")
    voice_switch.place(relx=0.75, rely=0.5, anchor=tk.CENTER)
    voice_lab = ctk.CTkLabel(master=frame_interface, text=eng[11], font=("Arial", 16))
    voice_lab.place(relx=0.17, rely=0.5, anchor=tk.CENTER)


    def model_info(*args):
        if selected_model.get() == 'gpt-3.5':
            del gpt_mod[0]
            gpt_mod.insert(0, 'gpt-3.5')

        if selected_engine.get() == 'turbo':
            del gpt_mod[2]
            gpt_mod.insert(2, 'turbo')
        elif selected_engine.get() == 'turbo-0301':
            del gpt_mod[2]
            gpt_mod.insert(2, 'turbo-0301')
        del gpt_model[0]
        gpt_model.append(gpt_mod[0]+gpt_mod[1]+gpt_mod[2])
        print(f'Model: {gpt_mod[0]+gpt_mod[1]+gpt_mod[2]}')
        with open('settings.py', 'w') as configfile:
            configfile.write(f"import openai\n")
            configfile.write(f"\n")
            if openai.api_key.startswith('sk-') and len(openai.api_key) == 51:
                configfile.write(f"openai.api_key = '{openai.api_key}'\n")
            else:
                configfile.write(f"openai.api_key = ''\n")
            configfile.write(f"api_key = openai.api_key\n")
            configfile.write(f"font_save = {font_save}\n")
            configfile.write(f"voice_save = {voice_save}\n")
            configfile.write(f"lang_save = {lang_save}\n")
            configfile.write(f"theme_save = {theme_save}\n")
            configfile.write(f"gpt_mod = {gpt_mod}\n")
            configfile.write(f"gpt_model = {gpt_model}\n")
            configfile.write(f"gpt_parameters = {gpt_parameters}\n")
            configfile.write(f"save_folder = '{save_folder}'\n")
            configfile.write(f"ask_save = True\n")
            configfile.write(f"save_or_no = True\n")




    model = ['gpt-3.5']
    selected_model = ctk.StringVar(value=gpt_mod[0])
    model_menu = ctk.CTkOptionMenu(master=frame_settings, values=model, variable=selected_model, width=100, command=model_info)
    model_menu.place(relx=0.375, rely=0.65, anchor=tk.CENTER)
    model_lab = ctk.CTkLabel(frame_settings, text=eng[12])
    model_lab.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

    engine_model = ['turbo', 'turbo-0301']
    selected_engine = ctk.StringVar(value=gpt_mod[2])
    engine_menu = ctk.CTkOptionMenu(master=frame_settings, values=engine_model, variable=selected_engine, width=100, command=model_info)
    engine_menu.place(relx=0.625, rely=0.65, anchor=tk.CENTER)


    def token_event(value):
        print(int(value))
        token_counter.configure(text=int(value))
        del gpt_parameters[0]
        gpt_parameters.insert(0, int(value))
        with open('settings.py', 'w') as configfile:
            configfile.write(f"import openai\n")
            configfile.write(f"\n")
            if openai.api_key.startswith('sk-') and len(openai.api_key) == 51:
                configfile.write(f"openai.api_key = '{openai.api_key}'\n")
            else:
                configfile.write(f"openai.api_key = ''\n")
            configfile.write(f"api_key = openai.api_key\n")
            configfile.write(f"font_save = {font_save}\n")
            configfile.write(f"voice_save = {voice_save}\n")
            configfile.write(f"lang_save = {lang_save}\n")
            configfile.write(f"theme_save = {theme_save}\n")
            configfile.write(f"gpt_mod = {gpt_mod}\n")
            configfile.write(f"gpt_model = {gpt_model}\n")
            configfile.write(f"gpt_parameters = {gpt_parameters}\n")
            configfile.write(f"save_folder = '{save_folder}'\n")
            configfile.write(f"ask_save = True\n")
            configfile.write(f"save_or_no = True\n")
    token_counter = ctk.CTkLabel(frame_settings, text=gpt_parameters[0])
    token_counter.place(relx=0.8, rely=0.75, anchor=ctk.CENTER)
    token_lab = ctk.CTkLabel(frame_settings, text=eng[13])
    token_lab.place(relx=0.125, rely=0.75, anchor=ctk.CENTER)
    token = ctk.CTkSlider(master=frame_settings, from_=100, to=4000, number_of_steps=390, command=token_event)
    token.place(relx=0.5, rely=0.75, anchor=ctk.CENTER)
    token.set(float(gpt_parameters[0]))


    def temp_event(value):
        print(value)
        temp_counter.configure(text=value)
        del gpt_parameters[1]
        gpt_parameters.insert(1, float(value))
        with open('settings.py', 'w') as configfile:
            configfile.write(f"import openai\n")
            configfile.write(f"\n")
            if openai.api_key.startswith('sk-') and len(openai.api_key) == 51:
                configfile.write(f"openai.api_key = '{openai.api_key}'\n")
            else:
                configfile.write(f"openai.api_key = ''\n")
            configfile.write(f"api_key = openai.api_key\n")
            configfile.write(f"font_save = {font_save}\n")
            configfile.write(f"voice_save = {voice_save}\n")
            configfile.write(f"lang_save = {lang_save}\n")
            configfile.write(f"theme_save = {theme_save}\n")
            configfile.write(f"gpt_mod = {gpt_mod}\n")
            configfile.write(f"gpt_model = {gpt_model}\n")
            configfile.write(f"gpt_parameters = {gpt_parameters}\n")
            configfile.write(f"save_folder = '{save_folder}'\n")
            configfile.write(f"ask_save = True\n")
            configfile.write(f"save_or_no = True\n")
    temp_counter = ctk.CTkLabel(frame_settings, text=gpt_parameters[1])
    temp_counter.place(relx=0.8, rely=0.85, anchor=ctk.CENTER)
    temp_lab = ctk.CTkLabel(frame_settings, text=eng[14])
    temp_lab.place(relx=0.125, rely=0.85, anchor=ctk.CENTER)
    temp = ctk.CTkSlider(master=frame_settings, from_=0.0, to=1.0, command=temp_event)
    temp.place(relx=0.5, rely=0.85, anchor=ctk.CENTER)
    temp.set(float(gpt_parameters[1]))



    def saves(*args):
        if theme_save[0] == 'Light':
            ctk.set_appearance_mode('Light')
            output_text.configure(fg_color='#f7f7f8', text_color='black')
            app.configure(fg_color='#ffffff')
            frame.configure(fg_color='#ffffff')
            input_entry.configure(fg_color='#ffffff', text_color='black')
            window.configure(fg_color='#ffffff')
            api_entry.configure(fg_color='#ffffff', text_color='black')
            api_lab.configure(fg_color='#f7f7f8', text_color='black')
            theme_label.configure(fg_color='#f7f7f8', text_color='black')
            chat_settings.configure(fg_color='#f7f7f8', text_color='black')
            interface.configure(fg_color='#f7f7f8', text_color='black')
            frame_settings.configure(fg_color='#f7f7f8')
            frame_interface.configure(fg_color='#f7f7f8')
            lang_lab.configure(fg_color='#f7f7f8', text_color='black')
            voice_lab.configure(fg_color='#f7f7f8', text_color='black')
            model_lab.configure(fg_color='#f7f7f8', text_color='black')
            token_lab.configure(fg_color='#f7f7f8', text_color='black')
            token_counter.configure(fg_color='#f7f7f8', text_color='black')
            temp_lab.configure(fg_color='#f7f7f8', text_color='black')
            temp_counter.configure(fg_color='#f7f7f8', text_color='black')
        elif theme_save[0] == 'Dark':
            ctk.set_appearance_mode("dark")
            output_text.configure(fg_color='#454553', text_color='#d2cab4')
            app.configure(fg_color='#363640')
            frame.configure(fg_color='#363640')
            input_entry.configure(fg_color='#363640', text_color='#d2cab4')
            window.configure(fg_color='#363640')
            api_entry.configure(fg_color='#363640', text_color='#d2cab4')
            api_lab.configure(fg_color='#454553', text_color='#d2cab4')
            theme_label.configure(fg_color='#454553', text_color='#d2cab4')
            chat_settings.configure(fg_color='#454553', text_color='#d2cab4')
            interface.configure(fg_color='#454553', text_color='#d2cab4')
            frame_settings.configure(fg_color='#454553')
            frame_interface.configure(fg_color='#454553')
            lang_lab.configure(fg_color='#454553', text_color='#d2cab4')
            voice_lab.configure(fg_color='#454553', text_color='#d2cab4')
            model_lab.configure(fg_color='#454553', text_color='#d2cab4')
            token_lab.configure(fg_color='#454553', text_color='#d2cab4')
            token_counter.configure(fg_color='#454553', text_color='#d2cab4')
            temp_lab.configure(fg_color='#454553', text_color='#d2cab4')
            temp_counter.configure(fg_color='#454553', text_color='#d2cab4')

        if lang_save[0] == 'English':
            chat_settings.configure(text=eng[2])
            interface.configure(text=eng[3])
            api_lab.configure(text=eng[8])
            api_btn.configure(text=eng[9])
            theme_label.configure(text=eng[4])
            lang_lab.configure(text=eng[10])
            voice_lab.configure(text=eng[11])
            model_lab.configure(text=eng[12])
            token_lab.configure(text=eng[13])
            temp_lab.configure(text=eng[14])
            theme_label.place(relx=0.115, rely=0.3, anchor=tk.CENTER)
            lang_lab.place(relx=0.175, rely=0.4, anchor=tk.CENTER)
            voice_lab.place(relx=0.17, rely=0.5, anchor=tk.CENTER)
        elif lang_save[0] == 'Russian':
            chat_settings.configure(text=rus[2])
            interface.configure(text=rus[3])
            api_lab.configure(text=rus[8])
            api_btn.configure(text=rus[9])
            theme_label.configure(text=rus[4])
            lang_lab.configure(text=rus[10])
            voice_lab.configure(text=rus[11])
            model_lab.configure(text=rus[12])
            token_lab.configure(text=rus[13])
            temp_lab.configure(text=rus[14])
            theme_label.place(relx=0.1, rely=0.3, anchor=tk.CENTER)
            lang_lab.place(relx=0.1, rely=0.4, anchor=tk.CENTER)
            voice_lab.place(relx=0.14, rely=0.5, anchor=tk.CENTER)
        elif lang_save[0] == 'Spanish':
            chat_settings.configure(text=esp[2])
            interface.configure(text=esp[3])
            api_lab.configure(text=esp[8])
            api_btn.configure(text=esp[9])
            theme_label.configure(text=esp[4])
            lang_lab.configure(text=esp[10])
            voice_lab.configure(text=esp[11])
            model_lab.configure(text=esp[12])
            token_lab.configure(text=esp[13])
            temp_lab.configure(text=esp[14])
            theme_label.place(relx=0.1, rely=0.3, anchor=tk.CENTER)
            lang_lab.place(relx=0.125, rely=0.4, anchor=tk.CENTER)
            voice_lab.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
        elif lang_save[0] == 'German':
            chat_settings.configure(text=deu[2])
            interface.configure(text=deu[3])
            api_lab.configure(text=deu[8])
            api_btn.configure(text=deu[9])
            theme_label.configure(text=deu[4])
            lang_lab.configure(text=deu[10])
            voice_lab.configure(text=deu[11])
            model_lab.configure(text=deu[12])
            token_lab.configure(text=deu[13])
            temp_lab.configure(text=deu[14])
            theme_label.place(relx=0.115, rely=0.3, anchor=tk.CENTER)
            lang_lab.place(relx=0.135, rely=0.4, anchor=tk.CENTER)
            voice_lab.place(relx=0.17, rely=0.5, anchor=tk.CENTER)
        elif lang_save[0] == 'Turkish':
            chat_settings.configure(text=tur[2])
            interface.configure(text=tur[3])
            api_lab.configure(text=tur[8])
            api_btn.configure(text=tur[9])
            theme_label.configure(text=tur[4])
            lang_lab.configure(text=tur[10])
            voice_lab.configure(text=tur[11])
            model_lab.configure(text=tur[12])
            token_lab.configure(text=tur[13])
            temp_lab.configure(text=tur[14])
            theme_label.place(relx=0.115, rely=0.3, anchor=tk.CENTER)
            lang_lab.place(relx=0.078, rely=0.4, anchor=tk.CENTER)
            voice_lab.place(relx=0.225, rely=0.5, anchor=tk.CENTER)
        elif lang_save[0] == 'Ukrainian':
            chat_settings.configure(text=ukr[2])
            interface.configure(text=ukr[3])
            api_lab.configure(text=ukr[8])
            api_btn.configure(text=ukr[9])
            theme_label.configure(text=ukr[4])
            lang_lab.configure(text=ukr[10])
            voice_lab.configure(text=ukr[11])
            model_lab.configure(text=ukr[12])
            token_lab.configure(text=ukr[13])
            temp_lab.configure(text=ukr[14])
            theme_label.place(relx=0.1, rely=0.3, anchor=tk.CENTER)
            lang_lab.place(relx=0.1, rely=0.4, anchor=tk.CENTER)
            voice_lab.place(relx=0.18, rely=0.5, anchor=tk.CENTER)
    saves()

    if theme_save[0] == 'Light':
        ctk.set_appearance_mode('Light')
        window.configure(fg_color='#ffffff')
        api_entry.configure(fg_color='#ffffff', text_color='black')
        api_lab.configure(fg_color='#f7f7f8', text_color='black')
        theme_label.configure(fg_color='#f7f7f8', text_color='black')
        chat_settings.configure(fg_color='#f7f7f8', text_color='black')
        interface.configure(fg_color='#f7f7f8', text_color='black')
        frame_settings.configure(fg_color='#f7f7f8')
        frame_interface.configure(fg_color='#f7f7f8')
        lang_lab.configure(fg_color='#f7f7f8', text_color='black')
        voice_lab.configure(fg_color='#f7f7f8', text_color='black')
        model_lab.configure(fg_color='#f7f7f8', text_color='black')
        token_lab.configure(fg_color='#f7f7f8', text_color='black')
        token_counter.configure(fg_color='#f7f7f8', text_color='black')
        temp_lab.configure(fg_color='#f7f7f8', text_color='black')
        temp_counter.configure(fg_color='#f7f7f8', text_color='black')
    elif selected_option.get() == 'Dark':
        ctk.set_appearance_mode("dark")
        window.configure(fg_color='#363640')
        api_entry.configure(fg_color='#363640', text_color='#d2cab4')
        api_lab.configure(fg_color='#454553', text_color='#d2cab4')
        theme_label.configure(fg_color='#454553', text_color='#d2cab4')
        chat_settings.configure(fg_color='#454553', text_color='#d2cab4')
        interface.configure(fg_color='#454553', text_color='#d2cab4')
        frame_settings.configure(fg_color='#454553')
        frame_interface.configure(fg_color='#454553')
        lang_lab.configure(fg_color='#454553', text_color='#d2cab4')
        voice_lab.configure(fg_color='#454553', text_color='#d2cab4')
        model_lab.configure(fg_color='#454553', text_color='#d2cab4')
        token_lab.configure(fg_color='#454553', text_color='#d2cab4')
        token_counter.configure(fg_color='#454553', text_color='#d2cab4')
        temp_lab.configure(fg_color='#454553', text_color='#d2cab4')
        temp_counter.configure(fg_color='#454553', text_color='#d2cab4')








def menu(*args):


    if selected_menu.get() == 'Help & FAQ':
        
        if lang_save[0] == 'English':

            confirmed = CTkMessagebox(title=eng[15],
                                      message=eng[16],
                                      icon="question", option_1="No", option_2="Yes")

        elif lang_save[0] == 'Russian':
            confirmed = CTkMessagebox(title=rus[15],
                                      message=rus[16],
                                      icon="question", option_1="No", option_2="Yes")

        elif lang_save[0] == 'Spanish':
            confirmed = CTkMessagebox(title=esp[15],
                                      message=esp[16],
                                      icon="question", option_1="No", option_2="Yes")

        elif lang_save[0] == 'German':
            confirmed = CTkMessagebox(title=deu[15],
                                      message=deu[16],
                                      icon="question", option_1="No", option_2="Yes")

        elif lang_save[0] == 'Turkish':
            confirmed = CTkMessagebox(title=tur[15],
                                      message=tur[16],
                                      icon="question", option_1="No", option_2="Yes")

        else:
            confirmed = CTkMessagebox(title=ukr[15],
                                      message=ukr[16],
                                      icon="question", option_1="No", option_2="Yes")


        if confirmed.get() == 'Yes':
            webbrowser.open_new("https://help.openai.com/en/collections/3742473-chatgpt")



    elif selected_menu.get() == 'Clear conversations':
        output_text.configure(state="normal")
        output_text.delete("1.0", ctk.END)
        output_text.configure(state="disabled")
    elif selected_menu.get() == 'Settings':
        settings()



options = ['Help & FAQ', 'Settings']
selected_menu = ctk.StringVar(value='Settings')
selected_menu.trace_add("write", menu)
option = ctk.CTkOptionMenu(master=app, values=options, variable=selected_menu, width=1)
option.pack(side="left", padx=10, pady=10)


# Создание виджета Entry для ввода вопросов
input_entry = ctk.CTkEntry(app, width=30, font=("Arial", 12))
input_entry.pack(side="left", fill="x", expand=True, padx=10, pady=10)
input_entry.bind("<Return>", lambda event: send_message())
input_entry.focus()




# Создание кнопки для отправки вопроса
send_image = ctk.CTkImage(light_image=Image.open("images\send.png"),
                          dark_image=Image.open("images\send.png"),
                          size=(20, 20))
submit_button = ctk.CTkButton(app, text=" ", width=1, image=send_image, command=lambda: send_message())
submit_button.pack(side="right", padx=10, pady=10)


output_text.configure(fg_color='#f7f7f8', text_color='black')
app.configure(fg_color='#ffffff')
frame.configure(fg_color='#ffffff')
input_entry.configure(fg_color='#ffffff', text_color='black')

def main():
    dialog = []  # Хранение сообщений диалога

    def save_dialog(dialog, file_path):
        # Функция сохранения диалога в файл
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(dialog))


    def on_closing(*args):

        text_content = output_text.get("1.0",
                                       tk.END).strip()  # Получение содержимого текстового поля и удаление пробелов
        if (ask_save == True and save_or_no == True) and text_content: # Проверка на наличие символов
            dialog.extend(text_content.splitlines())  # Расширение диалога с текстом сообщений
            if lang_save[0] == 'English':
                confirmed = CTkMessagebox(title="Confirmation", message="Do you want to save the dialogue?",
                                          icon="question", option_1="Cancel", option_2="No", option_3="Yes")
            elif lang_save[0] == 'Russian':
                confirmed = CTkMessagebox(title="Сохранение", message="Сохранить диалог?",
                                          icon="question", option_1="Cancel", option_2="No", option_3="Yes")
            elif lang_save[0] == 'Spanish':
                confirmed = CTkMessagebox(title="Confirmación", message="¿Desea guardar el diálogo?",
                                          icon="question", option_1="Cancel", option_2="No", option_3="Yes")
            elif lang_save[0] == 'German':
                confirmed = CTkMessagebox(title="Speichern", message="Möchten Sie den Dialog speichern?",
                                          icon="question", option_1="Cancel", option_2="No", option_3="Yes")
            elif lang_save[0] == 'Turkish':
                confirmed = CTkMessagebox(title="Kaydetme", message="Diyalogu kaydetmek istiyor musunuz?",
                                          icon="question", option_1="Cancel", option_2="No", option_3="Yes")
            else:
                confirmed = CTkMessagebox(title="Збереження", message="Бажаєте зберегти діалог?",
                                          icon="question", option_1="Cancel", option_2="No", option_3="Yes")
            if confirmed.get() == 'Yes':
                current_datetime = datetime.now()
                file_name = current_datetime.strftime('save' + '%d.%m.%Y_%H-%M-%S') + '.txt'
                # Создание папки, если она не существует
                folder_path = save_folder
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                file_path = os.path.join(folder_path, file_name)
                save_dialog(dialog, file_path)
                app.destroy()
            elif confirmed.get() == 'No':
                app.destroy()


        elif (save_or_no == True and ask_save == False) and text_content:
            current_datetime = datetime.now()
            file_name = current_datetime.strftime('save' + '%d.%m.%Y_%H-%M-%S') + '.txt'
            # Создание папки, если она не существует
            folder_path = save_folder
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            file_path = os.path.join(folder_path, file_name)
            save_dialog(dialog, file_path)
            app.destroy()
        else:
            confirmed = CTkMessagebox(title="Exit", message="Exit?",
                                      icon="question", option_1="Cancel", option_2="Ok")
            if confirmed.get() == 'Ok':
                app.destroy()



    app.protocol("WM_DELETE_WINDOW", on_closing)

main()





app_theme()


app.mainloop()

