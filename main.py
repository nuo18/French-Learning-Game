import tkinter as tk
from popup import *

#? Flashcard Popup
def open_flashcards():
    FlashcardPopup(root)
    print("Opening flashcards popup window...")

#? Translator Popup
def open_translator():
    TranslatorPopup(root)
    print("Opening translator window...")

#? Game Popup
def open_game():
    GamePopup(root)
    print("Opening game popup window...")

#? Help Popup
def open_addwords():
    AddWordPopup(root)
    print("Opening add words popup window...")

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
help_button = tk.Button(button_frame, text="Add", command=open_addwords, fg="white", bg="#6f42c1", padx=20, pady=10, bd=0, activebackground="#563d7c")
help_button.configure(relief="flat", overrelief="solid")
help_button.pack(pady=10)

# Create the "Exit" button
exit_button = tk.Button(root, text="Exit", command=root.quit, fg="white", bg="#393939", padx=20, pady=10, bd=0, activebackground="#1c1f23")
exit_button.configure(relief="flat", overrelief="solid")
exit_button.pack(side="bottom", pady=20)

# Run the main event loop
root.mainloop()
