import tkinter as tk
from popup import *

# Define the function to create a popup window for the "Flashcards" button
def open_flashcards():
    FlashcardPopup(root)
    print("Opening flashcards popup window...")

# Define the function to create a popup window for the "Translator" button
def open_translator():
    TranslatorPopup(root)
    print("Opening translator window...")

# Define the function to create a popup window for the "Game" button
def open_game():
    # This is where you would put the code to create the "Game" popup window
    GamePopup(root)
    print("Opening game popup window...")

# Define the function to create a popup window for the "Help" button
def open_help():
    popup = tk.Toplevel()
    popup.configure(bg='#24292e')
    popup.geometry('400x600')
    popup.title("Help")
    
    #Title
    label = tk.Label(popup, text='Help Section', bg='#24292e', fg='#ffffff', font=("helvetica 30 bold"))
    label.pack(padx=20, pady=20)
    #Flashcard
    label2 = tk.Label(popup, text='Click Flashcard to learn new French Words', bg='#24292e', fg='#ffffff', font=("helvetica 18"), wraplength=360, justify="center")
    label2.pack(padx=20, pady=20)
    #Translator
    label3 = tk.Label(popup, text='Click Translator to use the in-built French to English Translator', bg='#24292e', fg='#ffffff', font=("helvetica 18"), wraplength=360, justify="center")
    label3.pack(padx=20, pady=20)
    #Game
    label4 = tk.Label(popup, text='Click Game to revise French Words', bg='#24292e', fg='#ffffff', font=("helvetica 18"), wraplength=360, justify="center")
    label4.pack(padx=20, pady=20)
    #Exit
    label5 = tk.Label(popup, text='Click Exit to exit this app', bg='#24292e', fg='#ffffff', font=("helvetica 18"), wraplength=360, justify="center")
    label5.pack(padx=20, pady=20)

    popup.mainloop()

# Create the main window
root = tk.Tk()
root.title("French Learning App")
root.geometry("400x600")
root.configure(bg="#24292e")

# Create a frame to hold the buttons
button_frame = tk.Frame(root, bg="#24292e")
button_frame.pack(pady=30)

# Create the "Flashcards" button
flashcards_button = tk.Button(button_frame, text="Flashcards", command=open_flashcards, fg="white", bg="#0366d6", padx=20, pady=10, bd=0, activebackground="#034ea2")
flashcards_button.configure(relief="flat", overrelief="solid")
flashcards_button.pack(pady=10)

# Create the "Translator" button
translator_button = tk.Button(button_frame, text="Translator", command=open_translator, fg="white", bg="#28a745", padx=20, pady=10, bd=0, activebackground="#1e7e34")
translator_button.configure(relief="flat", overrelief="solid")
translator_button.pack(pady=10)

# Create the "Game" button
game_button = tk.Button(button_frame, text="Game", command=open_game, fg="white", bg="#d73a49", padx=20, pady=10, bd=0, activebackground="#c23944")
game_button.configure(relief="flat", overrelief="solid")
game_button.pack(pady=10)

# Create the "Help" button
help_button = tk.Button(button_frame, text="Help", command=open_help, fg="white", bg="#6f42c1", padx=20, pady=10, bd=0, activebackground="#563d7c")
help_button.configure(relief="flat", overrelief="solid")
help_button.pack(pady=10)

# Create the "Exit" button
exit_button = tk.Button(root, text="Exit", command=root.quit, fg="white", bg="#393939", padx=20, pady=10, bd=0, activebackground="#1c1f23")
exit_button.configure(relief="flat", overrelief="solid")
exit_button.pack(side="bottom", pady=20)

# Run the main event loop
root.mainloop()
