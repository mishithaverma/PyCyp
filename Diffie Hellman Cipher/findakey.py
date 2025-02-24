# Step 1: Input prime number p
p = int(input("Enter prime number p: "))

# Step 1.1: Check if p is prime using loops
is_prime = True
if p <= 1:
    is_prime = False
elif p == 2:
    is_prime = True
elif p % 2 == 0:
    is_prime = False
else:
    # Check divisors from 3 to sqrt(p)
    i = 3
    while i * i <= p:
        if p % i == 0:
            is_prime = False
            break
        i += 2

if not is_prime:
    print("Error: p must be a prime number.")
    exit()

# Step 2: Input base g and check if it's primitive root
g = int(input("Enter base g: "))

# Step 2.1: Check primitive root requirements
phi = p - 1  # For prime p, φ(p) = p-1

# Find prime factors of φ(p) using loops
factors = set()
temp = phi

# Factor out 2s
while temp % 2 == 0:
    factors.add(2)
    temp //= 2

# Factor out odd numbers
i = 3
while i * i <= temp:
    while temp % i == 0:
        factors.add(i)
        temp //= i
    i += 2
if temp > 2:
    factors.add(temp)

# Check primitive root condition using loops
is_primitive = True
for factor in factors:
    # Calculate (g^(φ(p)/factor)) mod p
    exponent = phi // factor
    result = 1
    base = g % p
    # Modular exponentiation using loop
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % p
        exponent = exponent // 2
        base = (base * base) % p
    if result == 1:
        is_primitive = False
        break

if not is_primitive:
    print(f"Error: {g} is not a primitive root of {p}")
    exit()

# Step 3: Input secret numbers
a = int(input("Enter Alice's secret number a: "))
b = int(input("Enter Bob's secret number b: "))

# Step 4: Calculate public values
# Calculate g^a mod p
A = 1
base = g % p
exponent = a
while exponent > 0:
    if exponent % 2 == 1:
        A = (A * base) % p
    exponent = exponent // 2
    base = (base * base) % p

# Calculate g^b mod p
B = 1
base = g % p
exponent = b
while exponent > 0:
    if exponent % 2 == 1:
        B = (B * base) % p
    exponent = exponent // 2
    base = (base * base) % p

print(f"\nAlice sends to Bob: {A}")
print(f"Bob sends to Alice: {B}")

# Step 6 & 7: Calculate shared secret
# Alice computes (B^a mod p)
shared_alice = 1
base = B % p
exponent = a
while exponent > 0:
    if exponent % 2 == 1:
        shared_alice = (shared_alice * base) % p
    exponent = exponent // 2
    base = (base * base) % p

# Bob computes (A^b mod p)
shared_bob = 1
base = A % p
exponent = b
while exponent > 0:
    if exponent % 2 == 1:
        shared_bob = (shared_bob * base) % p
    exponent = exponent // 2
    base = (base * base) % p

print(f"\nShared key computed by Alice: {shared_alice}")
print(f"Shared key computed by Bob: {shared_bob}")

# Final verification
if shared_alice == shared_bob:
    print("\nSuccess! Shared keys match.")
else:
    print("\nError! Shared keys do not match.")