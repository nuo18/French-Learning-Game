# words.py

# define the file path for the word list file
WORD_FILE = "words.txt"

# read the words from the file
def load_words():
    try:
        with open(WORD_FILE, "r") as f:
            words = [line.strip() for line in f]
    except FileNotFoundError:
        words = []
    return words

# write the words to the file
def save_words(words):
    with open(WORD_FILE, "w") as f:
        for word in words:
            f.write(word + "\n")

# add a word to the list and save it to the file
def add_word(fre_word, eng_word):
    fre_words = load_words()
    eng_words = load_words()
    fre_words.append(fre_word)
    eng_words.append(eng_word)
    save_words(fre_words)
    save_words(eng_words)

# initialize the word lists
fre_words = load_words()
eng_words = load_words()
