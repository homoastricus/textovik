import tkinter as tk
import speech_recognition as sr
import pyperclip
import config

config = config.Config()


class SpeechRecognitionApp:
    def __init__(self, root, config):
        self.root = root
        self.root.title(config.app_title)
        self.root.geometry(str(config.app_width) + "x" + str(config.app_height))
        self.root.configure(bg=config.app_bg_color)
        self.create_widgets(config)

    def create_widgets(self, config):
        # Header
        header = tk.Label(self.root,
                          text=config.app_title,
                          font=(config.app_base_font, 16, "bold"),
                          bg='#283593',
                          fg='white',
                          pady=10)
        header.pack(fill=tk.X)

        # Microphone button
        mic_button = tk.Button(self.root,
                               text=config.mic_button_title,
                               command=self.recognize_speech,
                               font=(config.app_base_font, 12),
                               bg='#1a73e8',
                               borderwidth=0,
                               activebackground='#1070e0',
                               activeforeground='#ffffff',
                               cursor="hand2",
                               fg='#ffffff'
                               )
        mic_button.pack(pady=20, padx=20, ipadx=8, ipady=8)

        # Output Label
        self.output_label = tk.Label(self.root,
                                     text="",
                                     font=(config.app_base_font, 14),
                                     bg=config.app_bg_color
                                     )
        self.output_label.pack(pady=20)

        self.text = tk.Text(self.root,
                            width=100,
                            height=12,
                            bg='#ffffff',
                            fg='#444444',
                            font=(config.app_returned_text_font, 11)
                            )
        self.text.pack(pady=20)

        # copy clipboard button
        copy_button = tk.Button(self.root,
                                text=config.clipboard_button_title,
                                command=pyperclip.copy(config.last_translated),
                                font=(config.app_base_font, 12),
                                bg='#1a73e8',
                                borderwidth=0,
                                activebackground='#1070e0',
                                activeforeground='#ffffff',
                                cursor="hand2",
                                fg='#ffffff'
                                )
        copy_button.pack(pady=20, padx=20, ipadx=8, ipady=8)

        # Footer
        footer_frame = tk.Frame(self.root, bg='#283593', pady=10)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        github_link = tk.Label(footer_frame,
                               text="GitHub: " + config.github_url,
                               font=(config.app_base_font, 10),
                               bg='#283593',
                               fg='white',
                               cursor="hand2"
                               )
        github_link.pack()
        github_link.bind("<Button-1>", lambda e: self.open_link(config.github_url))

    def recognize_speech(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        try:
            with microphone as source:
                self.output_label.config(text=config.recognize_talk_title)
                self.root.update()  # message
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source)
                self.output_label.config(text=config.recognize_performing_title)
                self.root.update()  # message for processing speech
                self.text.delete(1.0, tk.END)
            text = recognizer.recognize_google(audio, language=config.default_lang)
            text_format = self.format_text(text)
            config.last_translated = text_format
            # self.output_label.config(text=f"Вы сказали: {text_format}")
            self.output_label.config(text=config.speechtotext_complete_title)
            self.text.insert(1.0, text_format)
            pyperclip.copy(text_format)

        except sr.RequestError:
            self.output_label.config(text=config.api_unavailable_title)
        except sr.UnknownValueError:
            self.output_label.config(text=config.cant_translate_title)

    def open_link(self, url):
        import webbrowser
        webbrowser.open_new(url)

    def format_text(self, text):
        for key, value in config.format_strings.items():
            text = text.replace(key, value)
        text = text.replace(" ,", ",")
        return text


if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechRecognitionApp(root, config)
    root.mainloop()
