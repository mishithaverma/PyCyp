import random

# Input for prime number p and base g
p = int(input("Enter a prime number p: ")) 
g = int(input("Enter a base g: ")) 

# Validate that p is prime 
if p <= 1:
    print(f"{p} is not a prime number. Please enter a valid prime number.")
else:
    is_prime = True
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            is_prime = False
            break

    if not is_prime:
        print(f"{p} is not a prime number. Please enter a valid prime number.")
    else:
        # Alice's secret number
        a = random.randint(1, p - 1)
        A = 1
        for _ in range(a):  # (g^a) % p using loops
            A = (A * g) % p

        # Bob's secret number
        b = random.randint(1, p - 1)
        B = 1
        for _ in range(b):  # (g^b) % p using loops
            B = (B * g) % p

        # Alice's key (B^a) % p using loops
        alice_key = 1
        for _ in range(a):
            alice_key = (alice_key * B) % p

        # Bob's key (A^b) % p using loops
        bob_key = 1
        for _ in range(b):
            bob_key = (bob_key * A) % p

        # Ensure both keys are the same
        if alice_key != bob_key:
            print("Keys do not match!")
        else:
            # results
            print(f"\nPrime (p): {p}")
            print(f"Base (g): {g}")
            print(f"Alice's secret (a): {a}")
            print(f"Bob's secret (b): {b}")
            print(f"Alice sends: {A}")
            print(f"Bob sends: {B}")
            print(f"Shared secret key: {alice_key}")
