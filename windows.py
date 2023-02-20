import tkinter as tk


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
        self.word_label = tk.Label(self.popup, text='', font=('Arial', 20), bg='#24292e', fg='white')
        self.translation_label = tk.Label(self.popup, text='', font=('Arial', 16), bg='#24292e', fg='white')
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