import pandas as pd

#reading the excel file
excel_file = pd.read_excel('words_database.xlsx')

# French Words
fre_words = excel_file['French'].tolist()
#English Words
eng_words = excel_file['English'].tolist()