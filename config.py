class Config(object):

    def __init__(self):
        # gui config
        self.app_title = 'Текстовик'
        self.app_base_font = 'Helvitica'
        self.app_returned_text_font = 'TimesNewRoman'
        self.app_width = 900
        self.app_height = 700
        self.app_bg_color = '#f0f0f0'
        self.github_url = "https://github.com/homoastricus/textovik"
        # speeach to text config
        self.last_translated = ''
        self.mic_button_title = "🎙️Записать текст"
        self.clipboard_button_title = "Скопировать в буфер обмена"
        self.recognize_talk_title = "Слушаю... пожалуйста, говорите"
        self.recognize_performing_title = "Обработка речи..."
        self.default_lang = 'ru-RU'
        self.api_unavailable_title = "API недоступно"
        self.cant_translate_title = "Не удалось распознать речь"
        self.speechtotext_complete_title = "Речь успешно преобразована в текст"
        self.format_strings = {
            "запятая": ",",
            " точка": ".",
            "двоеточие": ":",
            "вопросительный знак": "?",
            "восклицательный знак": "!",
            " тире": "-",
            "процент": "%",
            "процента": "%",
            "процентов": "%",
            "круглая скобка открылась": "(",
            "круглая скобка закрылась": ")",
            "двойная кавычка": "\"",
            "плюс": "+",
            "знак равенства": "=",
        }
