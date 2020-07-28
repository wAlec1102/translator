# -*- coding: utf-8 -*-
# !/usr/bin/python3

"""
    Author alec.wang
"""

from googletrans import Translator
import speech_recognition as sr


def translate(text):
    translator = Translator()
    translation = translator.translate(text=text, src='en', dest='zh-cn')
    print('translation:', text, '->', translation.text)


def convert_audio_to_text():
    recognizer = sr.Recognizer()
    file_name = '../resources/audio/english.wav'
    with sr.AudioFile(file_name) as source:
        audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data, language='en', show_all=True)


if __name__ == '__main__':
    results = convert_audio_to_text()['alternative']
    translate(results[0]['transcript'])
