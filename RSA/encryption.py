# Step 1: Accept two prime numbers from the user
p = int(input("Enter first prime number (p): "))
while True:
    if p < 2:
        is_prime = False
    else:
        is_prime = True
        # Check divisibility up to sqrt(p)
        for i in range(2, int(p**0.5) + 1):
            if p % i == 0:
                is_prime = False
                break
    if is_prime:
        break
    else:
        print("Not a prime. Re-enter.")
        p = int(input("Enter first prime number (p): "))

q = int(input("Enter second prime number (q): "))
while True:
    if q < 2:
        is_prime = False
    else:
        is_prime = True
        # Check divisibility up to sqrt(q)
        for i in range(2, int(q**0.5) + 1):
            if q % i == 0:
                is_prime = False
                break
    if is_prime:
        break
    else:
        print("Not a prime. Re-enter.")
        q = int(input("Enter second prime number (q): "))

# Step 2: Compute n and φ(n)
n = p * q
phi = (p - 1) * (q - 1)
print("\nCalculated values:")
print(f"n = {n}")
print(f"φ(n) = {phi}")

# Step 3: Find e starting from 3, checking coprimality
e = 3
found = False
while e < phi:
    # Check gcd(e, p-1) == 1
    a, b = e, (p-1)
    while b != 0:
        a, b = b, a % b
    gcd_e_p1 = a
    
    # Check gcd(e, q-1) == 1
    a, b = e, (q-1)
    while b != 0:
        a, b = b, a % b
    gcd_e_q1 = a
    
    # Check gcd(e, phi) == 1
    a, b = e, phi
    while b != 0:
        a, b = b, a % b
    gcd_e_phi = a
    
    if gcd_e_p1 == 1 and gcd_e_q1 == 1 and gcd_e_phi == 1:
        found = True
        break
    e += 2  # Increment to next odd number

if not found:
    print("\nError: No suitable 'e' found. Try different primes.")
    exit()

# Step 4: Compute d (modular inverse of e mod phi)
# Using Extended Euclidean Algorithm
a, b = e, phi
old_r, r = a, b
old_s, s = 1, 0
old_t, t = 0, 1

while r != 0:
    quotient = old_r // r
    old_r, r = r, old_r - quotient * r
    old_s, s = s, old_s - quotient * s
    old_t, t = t, old_t - quotient * t

if old_r != 1:
    print("\nError: Modular inverse does not exist. Choose different primes.")
    exit()
else:
    d = old_s % phi  # Ensure d is positive

print("\nGenerated keys:")
print(f"Public key (e, n): ({e}, {n})")
print(f"Private key (d, n): ({d}, {n})")

# Step 5: Encrypt message
message = input("\nEnter message to encrypt (letters only): ")
message = message.upper()

cipher = []
for char in message:
    if not char.isalpha():
        continue
    # Convert character to 0-based index (A=0, B=1, ..., Z=25)
    m = ord(char) - ord('A')
    
    # Compute c = m^e mod n using manual modular exponentiation
    c = 1
    base = m % n
    exp = e
    while exp > 0:
        if exp % 2 == 1:
            c = (c * base) % n
        exp = exp // 2
        base = (base * base) % n
    cipher.append(str(c))

print("\nEncrypted ciphertext:", " ".join(cipher))