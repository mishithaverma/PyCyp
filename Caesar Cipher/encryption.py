#encryption for caesar cipher
#taking input from user for plain text
p=(input("Enter Plain Text: "))
#taking input from user for key
k=int(input("Enter Key: "))
#function to encrypt the text

shiftedp= ""

for char in p: 
    if char.isalpha():
        newchar= chr(ord(char)+k)
        shiftedp += newchar
        print("Your Cipher Text: ",shiftedp)
        
    else: 
        shiftedp += char

# Wrap around logic for lowercase letters
if char.islower():
    newchar = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))

# Wrap around logic for uppercase letters
elif char.isupper():
    newchar = chr(((ord(char) - ord('A') + k) % 26) + ord('A'))

else:
    # Leave non-alphabet characters unchanged
    newchar = char