from tkinter import ttk
import tkinter as tk
from googletrans import Translator
import words
import random
import pandas as pd

#? For Flashcarp popup window
class FlashcardPopup:
    def __init__(self, parent):
        self.popup = tk.Toplevel(parent)
        self.popup.configure(bg='#24292e')
        self.popup.geometry('400x600')
        self.popup.title("Flashcard")
        self.parent = parent
        
        # Create labels to display the French word and translation
        self.word_label = tk.Label(self.popup, text='', font=('helvetica', 30), height=5, bg='#24292e', fg='white', borderwidth=2, relief="ridge", width=20)
        self.translation_label = tk.Label(self.popup, text='', font=('helvetica', 30), height=5, bg='#24292e', fg='#00FF0C', borderwidth=2, relief="ridge", width=20)
        self.word_label.pack(pady=10)
        self.translation_label.pack(pady=10)
        
        # Create buttons to show answer and go to the next word
        self.show_answer_button = tk.Button(self.popup, text='Show Answer', command=self.show_answer, bg='#0366d6', fg='white')
        self.show_answer_button.pack(pady=10)
        self.next_word_button = tk.Button(self.popup, text='Go Next', command=self.go_next, bg='#28a745', fg='white')
        self.next_word_button.pack(pady=10)
        
        # Initialize variables for word and translation
        self.words = words.fre_words
        self.translations = words.eng_words
        self.word_index = -1
        
        # Shuffle the order of the words and translations
        self.word_order = list(range(len(self.words)))
        random.shuffle(self.word_order)
        
        # Go to the first word
        self.go_next()

    def show_answer(self):
        # Show the translation of the French word
        self.translation_label.config(text=self.translations[self.word_order[self.word_index]])

    def go_next(self):
        # Go to the next word and update labels
        self.word_index = (self.word_index + 1) % len(self.words)
        self.word_label.config(text=self.words[self.word_order[self.word_index]])
        self.translation_label.config(text='')


#? For translator popup window
class TranslatorPopup:
    def __init__(self, parent):
        self.popup = tk.Toplevel(parent)
        self.popup.configure(bg='#24292e')
        self.popup.geometry('400x600')
        self.popup.title("Translator")
        self.parent = parent
        
        # Style for combobox
        self.style= ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground= "#28a745", background= "#6f42c1")
        
        # Input text label
        self.source_lb = tk.Label(self.popup, text="Input Text", font=('helvetica', 18), bg='#24292e', fg='white')
        self.source_lb.place(x=10, y=10)
        
        # This is where the user inputs their text
        self.source_txt = tk.Text(self.popup,font=("helvetica",12), background="#24292e", foreground="white")
        self.source_txt.place(x=10,y=40,height=240,width=380)
        
        # Button to translate
        self.trans_btn = tk.Button(self.popup, text="Translate", font=("helvetica", 13), bg="#034ea2", fg="white", command=self.translate)
        self.trans_btn.place(x=200, y=290)
        # Button to clear text
        self.clear_btn = tk.Button(self.popup, text="Clear", font=("helvetica", 13), bg="#d73a49", fg="white", command=self.clear)
        self.clear_btn.place(x=300, y=290)
        
        # Output text label
        self.dest_lb = tk.Label(self.popup, text="Output Text", font=('helvetica', 18), bg='#24292e', fg='white')
        self.dest_lb.place(x=10, y=320)
        
        # This is where the translated text is shown
        self.dest_txt = tk.Text(self.popup,font=("helvetica",12), background="#24292e", foreground="white")
        self.dest_txt.place(x=10,y=350,height=240,width=380)
        
        self.languages = ["English", "French"]  # Languages
        
        # The drop down menu to source language
        self.sor_list = ttk.Combobox(self.popup, value=self.languages)
        self.sor_list.place(x=290, y=20, height=20, width=100)
        self.sor_list.set("English")
        
        # The drop down menu to select destination language
        self.dest_list = ttk.Combobox(self.popup, value=self.languages)
        self.dest_list.place(x=290, y=330, height=20, width=100)
        self.dest_list.set("French")
    
    # Referenced https://pypi.org/project/googletrans/ for understanding the API
    # Inspiration: https://www.youtube.com/watch?v=SSnZSr_6e_A
    
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
    
    def change(self, text="type", src="English", dest="French"):
        text1 = text
        src1 = src
        dest1 = dest
        trans = Translator() # calls the Translator class
        trans1 = trans.translate(text1, src=src1, dest=dest1)

        return trans1.text


#? For Game popup window
class GamePopup:
    def __init__(self, parent):
        self.parent = parent
        self.popup = tk.Toplevel(parent)
        self.popup.geometry('400x600')
        self.popup.title("Game")
        self.popup.configure(bg='#24292e')

        self.words = words.fre_words
        self.translations = words.eng_words
        # Problem sovled -- Use temp and zip to have same shuffle for both the lists
        temp = list(zip(self.words, self.translations))
        random.shuffle(temp)
        self.words, self.translations = zip(*temp)
        self.words, self.translations = list(self.words), list(self.translations)
        # Variables to store score and highscore
        self.current_word_index = 0
        self.score = 0
        self.high_score = self.load_high_score()

        self.word_label = tk.Label(self.popup, text=self.words[self.current_word_index], font=('helvetica', 24), bg='#24292e', fg='#ffffff')
        self.word_label.pack(padx=20, pady=20)

        self.answer_entry = tk.Entry(self.popup, font=('helvetica', 18))
        self.answer_entry.pack(padx=20, pady=20)

        self.check_button = tk.Button(self.popup, text='Check', font=('helvetica', 18), bg='#0366d6', fg='#ffffff', command=self.check_answer)
        self.check_button.pack(padx=20, pady=20)

        self.next_button = tk.Button(self.popup, text='Next', font=('helvetica', 18), bg='#28a745', fg='#ffffff', command=self.next_que)
        self.next_button.pack(padx=20, pady=20)

        self.feedback_label = tk.Label(self.popup, text='', font=('helvetica', 18), bg='#24292e', fg='#ffffff')
        self.feedback_label.pack(padx=20, pady=20)

        self.score_label = tk.Label(self.popup, text=f'Score: {self.score}', font=('helvetica', 18), bg='#24292e', fg='#ffffff')
        self.score_label.pack(padx=20, pady=20)

        self.high_score_label = tk.Label(self.popup, text=f'High Score: {self.high_score}', font=('helvetica', 18), bg='#24292e', fg='#ffffff')
        self.high_score_label.pack(padx=20, pady=20)

    def load_high_score(self):
        try:
            with open('high_score.txt', 'r') as f:
                high_score = int(f.read().strip()) # Reads the high score from the file and converts it to an integer
        except FileNotFoundError:
            high_score = 0 # If the file doesn't exist, sets the high score to 0
        return high_score
    
    # This function checks the user's answer and updates the score accordingly
    def check_answer(self):
        answer = self.answer_entry.get()
        # Using if and else as the user might accidently enter empty field
        if answer.lower() == self.translations[self.current_word_index].lower()[1:]:
            self.feedback_label.config(text=f'Correct : {self.translations[self.current_word_index]}', fg='#00ff00')
            self.score += 1
            self.score_label.config(text=f'Score: {self.score}')
        else:
            self.feedback_label.config(text=f'Incorrect : {self.translations[self.current_word_index]}', fg='#ff0000')
        # deleting entries
        self.answer_entry.delete(0, tk.END)
    
    # Next Question button command
    def next_que(self):
        self.current_word_index = (self.current_word_index + 1) % len(self.words)
        self.word_label.config(text=self.words[self.current_word_index])
        self.feedback_label.config(text='')
        self.answer_entry.delete(0, tk.END)
    
    # Checking if current score is larger than the high score
    def __del__(self):
        if self.score > self.high_score:
            with open('high_score.txt', 'w') as f:
                f.write(str(self.score))

#? For Add Words popup window
class AddWordPopup:
    def __init__(self, parent):
        self.parent = parent
        self.popup = tk.Toplevel(parent)
        self.popup.geometry('400x600')
        self.popup.title("Add Words")
        self.popup.configure(bg='#24292e')
        
        # French Word Label
        self.frelable = tk.Label(self.popup, text="French Word", font=('helvetica', 25), bg='#24292e', fg='white')
        self.frelable.pack(pady=20)
        #Input
        self.fre_entry = tk.Entry(self.popup, font=('helvetica', 18))
        self.fre_entry.pack(pady=20)
        
        # English Word Label
        self.englable = tk.Label(self.popup, text="English Word", font=('helvetica', 25), bg='#24292e', fg='white')
        self.englable.pack(pady=20)
        #Input
        self.eng_entry = tk.Entry(self.popup, font=('helvetica', 18))
        self.eng_entry.pack(pady=20)
        
        #Buttons
        self.add_btn = tk.Button(self.popup, text="Add Words", font=("helvetica", 13), bg="#28a745", fg="white", pady=10, padx=20, command=self.add_words)
        self.add_btn.pack(pady=20)
        
        self.clear_btn = tk.Button(self.popup, text="Clear", font=("helvetica", 13), bg="#d73a49", fg="white", pady=10, padx=20, command=self.clear)
        self.clear_btn.pack(pady=20)
        
        #Feedback label
        self.feedback = tk.Label(self.popup, text="", font=('helvetica', 25), bg='#24292e', fg='white')
        self.feedback.pack(pady=20)
        
        
    #Functions
    def clear(self):
        self.fre_entry.delete(0, 'end')
        self.eng_entry.delete(0, 'end')
    
    def add_words(self):
        # Read existing data from excel file
        df = pd.read_excel('words_database.xlsx')
    
        # Get user input
        french_word = self.fre_entry.get()
        english_word = self.eng_entry.get()
        
        # Add user input to dataframe
        if len(french_word) == 0 or len(english_word) == 0:
            self.feedback.config(text="Please enter both words", fg="#d73a49")
        else:
            new_row = {'French': french_word, 'English': english_word}
            df = df.append(new_row, ignore_index=True)
            # Save dataframe to excel file
            df.to_excel('words_database.xlsx', index=False)
            
            # Message
            self.feedback.config(text="Word Added Successfully", fg="#28a745")
                    
            # Clear input fields
            self.clear()