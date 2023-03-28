# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


path_letter = "./Input/Letters/starting_letter.txt"
path_names = "./Input/Names/invited_names.txt"
PLACEHOLDER = "[name]"

with open(path_names, mode='r') as file_name:
    names_list = file_name.readlines()

for name in names_list:
    with open(path_letter, mode='r') as file:
        letter = file.read()
        new_letter = letter.replace('[name]', name.strip())
    path_new_letters = f"./Output/ReadyToSend/letter_for_{name.strip()}.txt"
    with open(path_new_letters, mode='w') as file:
        file.write(new_letter)
