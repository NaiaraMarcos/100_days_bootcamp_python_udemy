from Day_8.art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    len_alphabet = len(alphabet)
  
    if cipher_direction == 'decode':
        shift_amount *= -1
        len_alphabet *= -1
        
    for char in start_text:
        if char.isalpha():
            index_alphabet = alphabet.index(char)
            if ((index_alphabet + shift_amount) <= (len(alphabet)-1)) \
                and ((index_alphabet -  shift_amount) >= 0):
                end_text += alphabet[(index_alphabet + shift_amount)]
            else:
                end_text += alphabet[index_alphabet + shift_amount - len_alphabet]
        else:
            end_text += char
    print(f"The {cipher_direction} text is {end_text}")
    
continue_program = True
print(logo)
while continue_program == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % len(alphabet)
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
    cont_prog = (input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")).lower()
    if cont_prog == 'no':
        continue_program = False
        print('Goodbye!!!')