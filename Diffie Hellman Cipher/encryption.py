import random 
# number is prime 
def is_prime(n): 
    if n <= 1: 
        return False 
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0: 
            return False 
    return True 
 
# Input for prime number p and base g 
p = int(input("Enter a prime number p: ")) 
g = int(input("Enter a base g: ")) 
 
# Validate that p is prime 
if not is_prime(p): 
    print(f"{p} is not a prime number. Please enter a valid prime number.") 
else: 
     
    a = random.randint(1, p - 1)  # Alice's secret number 
    A = pow(g, a, p)  # (g^a) % p 
 
    b = random.randint(1, p - 1)  # Bob's secret number  
 
    B = pow(g, b, p)  # (g^b) % p 
 
    alice_key = pow(B, a, p)  # (B^a) % p 
 
    bob_key = pow(A, b, p)  # (A^b) % p 
 
    assert alice_key == bob_key, "Keys do not match!"  # Ensure both keys are the same 
 
    # results 
    print(f"\nPrime (p): {p}") 
    print(f"Base (g): {g}") 
    print(f"Alice's secret (a): {a}") 
    print(f"Bob's secret (b): {b}") 
    print(f"Alice sends: {A}") 
    print(f"Bob sends: {B}") 
    print(f"Shared secret key: {alice_key}") 