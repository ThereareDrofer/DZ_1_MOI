from models.VoiceRecognizer import SoundRecognizer
import tkinter as tk
from tkinter import filedialog as fd

class MainDialog:

    def construct_diaolog(self):
        self.diaolog = tk.Tk()
        self.diaolog.title("Translate voice")
        self.diaolog.geometry('700x500')
        self.diaolog.resizable(False, False)

        self.frame_1 = tk.Frame(self.diaolog, bg='#006633', height=300)
        self.frame_1.pack(side=tk.BOTTOM, fill=tk.X)

        self.load_btn = tk.Button(self.frame_1, text='       Open File      ', command=self.open_file_manager, fg='#0000ff')
        self.load_btn.pack(side=tk.LEFT, fill=tk.BOTH)

        self.translate_btn = tk.Button(self.frame_1, text='      Translate      ', command=self.translate_voice, fg='#0000ff')
        self.translate_btn.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.choose_file = tk.Label(self.frame_1, text='  <<< - Choose file', bg='#006633',fg='white')
        self.choose_file.pack(side=tk.LEFT, fill=tk.BOTH)\

        self.text_view = tk.Text(self.diaolog, bg='white', fg='black', wrap=tk.WORD)
        self.text_view.pack(side=tk.TOP, fill=tk.BOTH)

        self.diaolog.mainloop()

    def __init__(self):
        self.construct_diaolog()
        self.translate_file = ''

    def translate_voice(self):
        if self.translate_file != '':
            self.text_view.insert(0.0, SoundRecognizer.recognize(self.translate_file))
        else:
            self.text_view.insert(0.0, "There was some problems with translating your .wav file:(")

    def open_file_manager(self):
        file = fd.askopenfilename()
        if file != '':
            self.translate_file = file
            self.choose_file['text'] = self.translate_file


if __name__ == '__main__':
    pass
