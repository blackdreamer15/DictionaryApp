from tkinter import *
from tkinter import ttk
from dictionary_api import DictionaryAPI
from dictionary_json import DictionaryJSON

dict_json = DictionaryJSON()
# TODO: Replace words.csv with your filename


class DictionaryApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.pages = (HomePage, MeaningPage)
        self.dictionary_data = {
            'word': StringVar(),
        }
        for F in self.pages:
            frame = F(container, self, self.pages)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(HomePage)

    def get_page(self, classname):
        for page in self.frames.values():
            if str(page.__class__.__name__) == classname:
                return page
        return None

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.event_generate("<<show_frame>>")

    def to_meaning_page(self):
        self.show_frame(MeaningPage)


class HomePage(Frame):
    def __init__(self, parent, controller, pages):
        Frame.__init__(self, parent)
        self.controller = controller
        self.pages = pages
        new_image = PhotoImage(file="background.png")
        background = Label(self, image=new_image)
        background.place(x=0, y=0)
        background.image = new_image

        homeCanvas = Canvas(self)
        homeCanvas.pack(fill='both', expand=True)
        homeCanvas.create_image(0, 0, image=new_image, anchor='nw')
        homeCanvas.create_text(
            300, 40, text="\n\nDictionaryApp", font=("stellar", 55, "bold"))

        homeCanvas.create_text(300, 230, text="Enter Word",
                               font=("stellar", 20, "bold"))
        search_box = ttk.Entry(self, font=(
            "Helvetico", 16), textvariable=self.controller.dictionary_data['word'])
        search_box.place(x=130, y=250, width=370, height=40)

        search_image = PhotoImage(file="search.png")
        search_button = Button(self, image=search_image, bd=0, bg='whitesmoke', cursor='hand2',
                               command=lambda: controller.to_meaning_page())
        search_button.pack()
        search_button.place(x=460, y=252.5)
        search_button.image = search_image

        search_box.bind('<Return>', lambda d: controller.to_meaning_page())


class MeaningPage(Frame):
    def __init__(self, parent, controller, pages):
        Frame.__init__(self, parent)
        self.controller = controller
        self.pages = pages
        new_image = PhotoImage(file="meaning_page.png")
        background = Label(self, image=new_image)
        background.place(x=0, y=0)
        background.image = new_image
        self.meaningCanvas = Canvas(self)
        self.meaningCanvas.pack(fill='both', expand=True)
        self.meaningCanvas.create_image(0, 0, image=new_image, anchor='nw')
        self.bind("<<show_frame>>", self.update_frame)
        # self.meaning = Text(self, font=("Verdana", 8), bd=0)

        back_button = Button(self, text="Back", font=("Times_New_Roman", 15), bd=1, relief=GROOVE,
                             command=self.back_button, bg="light blue")
        back_button.place(x=300, y=540)

    def back_button(self):
        self.controller.dictionary_data['word'].set('')
        self.controller.show_frame(self.pages[0])

    def update_frame(self, event):
        value = self.controller.dictionary_data
        word = value['word'].get()
        word_data = dict_json.search_word(word)
        if type(word_data) is dict:
            self.meaning = Text(self, font=("arial", 12), bd=1)
            try:
                word_meaning = word_data["definition"]
            except:
                word_meaning= " "
            
            try:
                part_of_speech = word_data['partOfSpeech']
            except:
                part_of_speech= " "
            
            try:
                word_synonyms = ", ".join(word_data['synonyms'])
            except:
                word_synonyms= " "
            try :
                word_data['antonyms']
                word_antonyms = ", ".join(word_data['antonyms'])
            except:
                word_antonyms= "  "
            
            self.meaning.insert('end', word.title() + '\n')
            self.meaning.insert('end', '(' + part_of_speech.title() + ')\n\n')
            self.meaning.insert('end', 'Definition:\n')
            self.meaning.insert('end', word_meaning + '\n\n')

            if word_synonyms:
                self.meaning.insert('end', 'Synonym(s):\n')
                self.meaning.insert('end', word_synonyms + '\n\n')

            if word_antonyms:
                self.meaning.insert('end', 'Antonym(s):\n')
                self.meaning.insert('end', word_antonyms + '\n\n')
            self.meaning.config(state="disabled")

            self.meaning.tag_add('word', '1.0', '1.end')
            self.meaning.tag_add('function', '2.0', '2.end')
            self.meaning.tag_add('title', '4.0', '4.end')
            self.meaning.tag_add('title', '7.0', '7.end')
            self.meaning.tag_add('title', '10.0', '10.end')
            self.meaning.tag_add('title', '13.0', '13.end')
            self.meaning.tag_config('word', font='arial 20 bold')
            self.meaning.tag_config('function', foreground='blue')
            self.meaning.tag_config('title', foreground='blue', font='Verdana 12 bold')
            # self.meaning.tag_config('title1', font='arial 20 bold', foreground= "blue")
            self.meaning.place(x=65, y=35, width=500, height=500)
        else:
            self.meaning = Text(self, font=("arial", 12), bd=1)
            self.meaning.insert('end', '\n'+word_data)
            self.meaning.tag_add('caution', '1.0', '3.end')
            self.meaning.tag_add('close', '4.0', '4.end')
            self.meaning.tag_config('caution', foreground='red', font='Courier 12 bold')
            # self.meaning.tag_config('close', font='Verdana 12 bold')
            self.meaning.place(x=65, y=35, width=400, height=400 )


if __name__ == '__main__':
    app = DictionaryApp()
    app.geometry("626x626+100+30")
    app.resizable(False, False)
    app.title("Group 2 Dictionary")
    app.mainloop()
