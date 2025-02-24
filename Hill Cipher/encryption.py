#define the key matrix
k = [[3, 3], [2, 5]]

#input even plaintext
while True:
    p = input("Enter plaintext (even length only): ").strip().upper()
    if len(p) % 2 == 0 and len(p) > 0:
        break
    print("Invalid input! Plaintext must have even number of characters.")

#encryption process
c = ""
for i in range(0, len(p), 2):
    #convert character pair to numbers
    a = ord(p[i]) - ord('A')
    b = ord(p[i+1]) - ord('A')
    
    #matrix multiplication with key
    c1 = (k[0][0] * a + k[0][1] * b) % 26
    c2 = (k[1][0] * a + k[1][1] * b) % 26
    
    #convert back to letters
    c += chr(c1 + ord('A')) + chr(c2 + ord('A'))

#output result
print("Ciphertext:", c)