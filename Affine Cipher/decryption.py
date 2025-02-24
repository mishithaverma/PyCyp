#alphabets for decryption
alphabet="abcdefghijklmnopqrstuvwxyz"
# ask user to enter the cipher text
c= input("Enter Cipher Text: ")
#enter the values for a and b
a= int(input("Enter a: "))
b= int(input("Enter b: "))

# find the modular inverse of a such that (a * a_inv) % 26 == 1
for a_inv in range(2,25):
    if (a * a_inv) % 26 == 1:
        ainverse=a_inv

# print the modular inverse of 'a'
print(f"modular inverse of {a} is {ainverse}")

# initialize an empty string to store the decrypted text
p = ""

# loop through each character in the cipher text
for char in c:
    if char.isalpha():
        charlower=char.lower()

# find position of the character in the alphabet
        y= alphabet.index(charlower)

# decryption formula: (ainverse * (y - b)) % 26
        decryptedval = (ainverse*(y-b) % 26)

        decrypted = alphabet[decryptedval]

        p += decrypted

#resultant decrypted text
print("Decrypted Text: ",p)






