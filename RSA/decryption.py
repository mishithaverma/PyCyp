# Step 1: Accept private key (d, n)
d = int(input("Enter private key exponent (d): "))
n = int(input("Enter modulus (n): "))

# Step 2: Accept ciphertext
cipher_input = input("Enter ciphertext (space-separated numbers): ")
cipher_list = list(map(int, cipher_input.split()))

# Step 3: Decrypt each number
decrypted = []
for c in cipher_list:
    # Compute m = c^d mod n using manual modular exponentiation
    m = 1
    base = c % n
    exp = d
    while exp > 0:
        if exp % 2 == 1:
            m = (m * base) % n
        exp = exp // 2
        base = (base * base) % n
    # Convert m to character (A=0, B=1, ..., Z=25)
    decrypted_char = chr(m + ord('A'))
    decrypted.append(decrypted_char)

print("\nDecrypted message:", "".join(decrypted))