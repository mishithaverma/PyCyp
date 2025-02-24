# decryption for caesar cipher
# taking input from user for cipher text
c = input("Enter Cipher Text: ")
# taking input from user for key
k = int(input("Enter Key: "))

# function to decrypt the text
shiftedc = ""

for char in c:
    if char.isalpha():
        # wrap around logic for lowercase letters
        if char.islower():
            newchar = chr(((ord(char) - ord('a') - k) % 26) + ord('a'))
        # wrap around logic for uppercase letters
        elif char.isupper():
            newchar = chr(((ord(char) - ord('A') - k) % 26) + ord('A'))
            
        shiftedc += newchar  # store the new character to the result string
    else:
        shiftedc += char

print("Your Decrypted Text: ", shiftedc)
