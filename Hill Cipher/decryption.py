#original key matrix
k = [[3, 3], [2, 5]]

#calculate determinant
det = k[0][0] * k[1][1] - k[0][1] * k[1][0]

#find modular inverse of determinant
inv_det = None
for x in range(1, 26):
    if (det * x) % 26 == 1:
        inv_det = x
        break


#calculate adjugate matrix
adj = [
    [k[1][1], -k[0][1]],
    [-k[1][0], k[0][0]]
]

#convert adjugate to positive modulo 26
for i in range(2):
    for j in range(2):
        adj[i][j] = adj[i][j] % 26

#calculate inverse key matrix
inv_key = [[0]*2, [0]*2]
for i in range(2):
    for j in range(2):
        inv_key[i][j] = (adj[i][j] * inv_det) % 26

#decryption process
while True:
    c = input("Enter ciphertext (even length): ").upper().strip()
    if len(c) % 2 == 0 and len(c) > 0:
        break
    print("Invalid input! Must have even length")

p = ""
for i in range(0, len(c), 2):
    #convert to numbers
    c1 = ord(c[i]) - ord('A')
    c2 = ord(c[i+1]) - ord('A')
    
    #matrix multiplication with inverse key
    a = (inv_key[0][0] * c1 + inv_key[0][1] * c2) % 26
    b = (inv_key[1][0] * c1 + inv_key[1][1] * c2) % 26
    
    p += chr(a + ord('A')) + chr(b + ord('A'))

print("Decrypted text:", p)