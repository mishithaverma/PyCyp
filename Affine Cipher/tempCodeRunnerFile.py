is_prime= True
for i in range(2, a):
    if a % i == 0:
        is_prime = False
        break


if not is_prime:
    print(f"Error: {a} is not a prime number, Please enter a prime number")
else:
    print(f"{a} is a prime number")