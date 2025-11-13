def is_prime_basic(n):
    """Checks if a number n is prime using a basic iteration."""
    # 1 and numbers less than 1 are not prime
    if n <= 1:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # All other even numbers are not prime
    if n % 2 == 0:
        return False
    
    # Check for factors from 3 up to the square root of n, skipping even numbers
    # We only need to check up to the square root of n because if n has a factor 
    # greater than its square root, it must also have a factor less than its 
    # square root.
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False  # Found a factor, so it's not prime
        i += 2  # Skip even numbers
        
    return True # No factors found, so it is prime

# --- Example Usage ---
number1 = 17
number2 = 15

print(f"Is {number1} prime? {is_prime_basic(number1)}")
print(f"Is {number2} prime? {is_prime_basic(number2)}")
print(f"Is 2 prime? {is_prime_basic(2)}")
print(f"Is 1 prime? {is_prime_basic(1)}")
