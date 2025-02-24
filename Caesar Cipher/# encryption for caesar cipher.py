# encryption for caesar cipher
# taking input from user for plain text
p = input("Enter Plain Text: ")
# taking input from user for key
k = int(input("Enter Key: "))

# function to encrypt the text
shiftedp = ""

for char in p:
    if char.isalpha():
        # wrap around logic for lowercase letters
        if char.islower():
            newchar = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
        # wrap around logic for uppercase letters
        elif char.isupper():
            newchar = chr(((ord(char) - ord('A') + k) % 26) + ord('A'))
        
        shiftedp += newchar  #store the new character to the result string
    else:
        shiftedp += char

print("Your Cipher Text: ", shiftedp)
