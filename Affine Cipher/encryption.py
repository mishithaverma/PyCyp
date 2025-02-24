#alphabets for encryption
alphabets=("abcdefghijklmnopqrstuvwxyz")
# ask user to enter the plain text
p=input("Enter the Plain Text: ")
#enter the values for a and b
a=int(input("Enter a:"))
b=int(input("Enter b:"))


#check if a is a prime number
is_prime= True
for i in range(2, a):
    if a % i == 0:
        is_prime = False
        break

#if a is not a prime number then show an error message
if not is_prime:
    print(f"Error: {a} is not a prime number, Please enter a prime number")
else:
    print(f"{a} is a prime number")
#initialize an empty string to store cipher text
c=""
#loop through each character in the plain text
for char in p:
    if char.isalpha():
        charlower=char.lower()
#find position of the character in the alphabet
        x = alphabets.index(charlower)
#encryption formula: (a * x + b) % 26
        encryptionval = (a * x + b) % 26

        encryption= alphabets[encryptionval]

        c = c + encryption
#resultant cipher text
print("Encrypted text:", c)



