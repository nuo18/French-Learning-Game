import pandas as pd

#reading the excel file
excel_file = pd.read_excel('words_database.xlsx')

# French Words from the Excel sheet
fre_words = excel_file['French'].tolist()
#English Words from the excel sheet
eng_words = excel_file['English'].tolist()

# Learning Pandas: https://www.w3schools.com/python/pandas/default.asp