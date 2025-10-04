#TEST CASE 1
print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
step_count = 0

print("Sequence:", current_number, end=" ")

while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = current_number * 3 + 1
    
    print(current_number, end=" ")
    step_count += 1
print()
print("Steps:", step_count)
#TEST CASE 2
print()
print("=== Challenge 2: Prime Number Checker ===")
n = int(input("Enter a number: "))

print(f"Testing divisors from 2 to {n-1}...")

is_prime = True
for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not prime (divisible by {i})")
        is_prime = False
        break

if is_prime:
    print(f"{n} is prime!")
print()
