from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

play_again = True

while play_again == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  
  def encrypt_or_decrypt_message(text, shift, direction):
    new_text = ""

    for char in text:
      if char in alphabet:
        letter_idx = alphabet.index(char)
        if direction == 'encode':
          new_idx = letter_idx + shift
        elif direction == 'decode':
          new_idx = letter_idx - shift
        new_text += alphabet[new_idx]
      else:
        new_text += char
      
  
    print(f"The {direction}d text is {new_text}")


  
  
  encrypt_or_decrypt_message(text, shift, direction)   
  
  play_again_response = input("Would you like to play again? yes or no.\n")

  if play_again_response == 'no':
    play_again = False
    print("Goodbye")