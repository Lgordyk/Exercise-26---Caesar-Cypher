alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if shift >= 0:
  new_shift = 0
  divisible_num = 0
  new_shift = shift
  divisible_num = shift // 26
  divisible_num = int(divisible_num)
  new_shift = shift - (26 * divisible_num)

#print(f"{shift} divided by 26 is {divisible_num}")
#print(alphabet[alphabet.index(text) + new_shift])

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text,new_shift):
  letter = ""
  new_letter = ""
  encrypted_message = ""
  
  for letter in text:
    if letter == " ":
      encrypted_message = encrypted_message + " "
    else:
      encrypted_message = encrypted_message + alphabet[alphabet.index(letter) + new_shift]
  print(f"{encrypted_message}")
  
def decrypt(text,new_shift):
  letter = ""
  new_letter = ""
  decrypted_message = ""
  for letter in text:
    if letter == " ":
      decrypted_message = decrypted_message + " "
    elif alphabet[alphabet.index(letter)] <= "4":
      decrypted_message = decrypted_message + alphabet[alphabet.index(letter) + 21]
    elif alphabet[alphabet.index(letter)] > "4":
      decrypted_message = decrypted_message + alphabet[alphabet.index(letter) - new_shift]
  print(f"{decrypted_message}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == "encode":
  encrypt(text,new_shift)
elif direction == "decode":
  decrypt(text,new_shift)
else:
  print("You did not select a valid direction.")

