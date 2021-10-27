# Day 8/100 Caesar Cipher
import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# function that takes plain or cipher text, takes the shift input, and calculates shift number with the alphabet to encode/decode messages
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    
    if cipher_direction == 'decode':
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)        
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    
    print(f'Your {cipher_direction}d text is: {end_text}')
        

#input and while loop. calls the function above with the following input arguments
run_again = True
while run_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    run_check = input('Run again? Type yes or no.\n')
    if run_check == 'no':
        run_again = False
        print("\nThanks for using Aaron's Caesar Cipher!\n")