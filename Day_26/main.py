import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_phonetic_dict = {row['letter']: row['code'] for (index, row) in nato_data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word_input = input("Enter a word:").upper()
nato_word = [nato_phonetic_dict[letter] for letter in word_input]
print(nato_word)