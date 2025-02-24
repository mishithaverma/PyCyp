# function to decrypt a caesar cipher with a given key
def bruteforce(ciphertext, key):
    plaintext = ""  # to store the decrypted message
    for char in ciphertext:
        if char.isalpha():
            # decrypt for lowercase letters
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
            # decrypt for uppercase letters
            elif char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
            plaintext += decrypted_char
        else:
            # keep non-alphabet characters unchanged
            plaintext += char
    return plaintext


# accept cipher text from the user
ciphertext = input("Enter Cipher Text: ")

# try all keys from 0 to 25 and print the decrypted result
for key in range(26):
    decryptedtext = bruteforce(ciphertext, key)
    print("Key " + str(key) + ": " + decryptedtext)

