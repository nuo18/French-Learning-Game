from tkinter import ttk
import tkinter as tk
from googletrans import Translator


#todo Incoparate Excel sheet and words
#? For Flashcarp popup window
class FlashcardPopup:
    def __init__(self, parent):
        self.popup = tk.Toplevel(parent)
        self.popup.configure(bg='#24292e')
        self.popup.geometry('400x600')
        self.popup.title("Flashcard")
        self.parent = parent
        
        # Create labels to display the French word and translation
        self.word_label = tk.Label(self.popup, text='', font=('helvetica', 20), bg='#24292e', fg='white', borderwidth=2)
        self.translation_label = tk.Label(self.popup, text='', font=('helvetica', 20), bg='#24292e', fg='white')
        self.word_label.pack(pady=20)
        self.translation_label.pack(pady=10)
        
        # Create buttons to show answer and go to the next word
        self.show_answer_button = tk.Button(self.popup, text='Show Answer', command=self.show_answer, bg='#393939', fg='white')
        self.show_answer_button.pack(pady=10)
        self.next_word_button = tk.Button(self.popup, text='Go Next', command=self.go_next, bg='#393939', fg='white')
        self.next_word_button.pack(pady=10)
        
        # Initialize variables for word and translation
        self.words = ['Bonjour', 'Comment allez-vous?', 'Je m\'appelle', 'Merci', 'Oui', 'Non', 'Au revoir']
        self.translations = ['Hello', 'How are you?', 'My name is', 'Thank you', 'Yes', 'No', 'Goodbye']
        self.word_index = -1
        
        # Go to the first word
        self.go_next()

    def show_answer(self):
        # Show the translation of the French word
        self.translation_label.config(text=self.translations[self.word_index])

    def go_next(self):
        # Go to the next word and update labels
        self.word_index = (self.word_index + 1) % len(self.words)
        self.word_label.config(text=self.words[self.word_index])
        self.translation_label.config(text='')


#? For translator popup window
class TranslatorPopup:
    def __init__(self, parent):
        self.popup = tk.Toplevel(parent)
        self.popup.configure(bg='#24292e')
        self.popup.geometry('400x600')
        self.popup.title("Translator")
        self.parent = parent
        
        #Show lable
        #self.wel_label = tk.Label(self.popup, text='Translator', font=('helvetica', 20), bg='#24292e', fg='white')
        #self.wel_label.pack(padx=10)
        
        #?Style for combobox
        self.style= ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground= "#28a745", background= "#6f42c1")
        
        #input text label
        self.source_lb = tk.Label(self.popup, text="Input Text", font=('helvetica', 18), bg='#24292e', fg='white')
        self.source_lb.place(x=10, y=10)
        
        #this is where the user inputs their text
        self.source_txt = tk.Text(self.popup,font=("helvetica",12), background="#24292e", foreground="white")
        self.source_txt.place(x=10,y=40,height=240,width=380)
        
        #button to translate
        #todo add command
        self.trans_btn = tk.Button(self.popup, text="Translate", font=("helvetica", 13), bg="#034ea2", fg="white", command=self.translate)
        self.trans_btn.place(x=200, y=290)
        #button to clear text
        self.clear_btn = tk.Button(self.popup, text="Clear", font=("helvetica", 13), bg="#d73a49", fg="white", command=self.clear)
        self.clear_btn.place(x=300, y=290)
        
        #output text label
        self.dest_lb = tk.Label(self.popup, text="Output Text", font=('helvetica', 18), bg='#24292e', fg='white')
        self.dest_lb.place(x=10, y=320)
        
        #this is where the text translated is shown
        self.dest_txt = tk.Text(self.popup,font=("helvetica",12), background="#24292e", foreground="white")
        self.dest_txt.place(x=10,y=350,height=240,width=380)
        
        self.languages = ["English", "French"]
        
        #The drop down menu to select language
        self.sor_list = ttk.Combobox(self.popup, value=self.languages)
        self.sor_list.place(x=290, y=20, height=20, width=100)
        self.sor_list.set("English")
        
        
        self.dest_list = ttk.Combobox(self.popup, value=self.languages)
        self.dest_list.place(x=290, y=330, height=20, width=100)
        self.dest_list.set("French")
    
    def clear(self):
        self.source_txt.delete(1.0, 'end')
        self.dest_txt.delete(1.0, 'end')
    
    def translate(self):
        in_lang = self.sor_list.get() # gets the input language
        out_lang = self.dest_list.get() # gets the language that is will be outputted
        input_text = self.source_txt.get(1.0, tk.END) # text the user input that needs to be changed
        output_text = self.change(text=input_text, src=in_lang, dest=out_lang)
        self.dest_txt.delete(1.0, tk.END)
        self.dest_txt.insert(tk.END, output_text)
    
    
    def change(text="type", src="English", dest="French"):
        text1 = text
        src1 = src
        dest1 = dest
        trans = Translator() # calls the Translator class
        trans1 = trans.translate(text1, src=src1, dest=dest1)
        
        return trans1.text