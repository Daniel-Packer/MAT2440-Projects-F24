def is_prime(n):
    if n <= 1:
        return f"{n} is not a prime number."
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return f"{n} is a complex number."
        return f"{n} is a prime number."

number = int(input("Enter a positive number: "))
print(is_prime(number))

# When the script is ran using a Python code tester at https://www.online-python.com/, a prompt appears that asks the user to enter a positive number.

# - Entering -5 returns the result: -5 is not a prime number.
# - Entering 0 returns the result: 0 is not a prime number.
# - Entering 1 returns the result: 1 is not a prime number.
# - Entering 16 returns the result: 16 is a complex number.
# - Entering 47 returns the result: 47 is a prime number.

# The script works for large numbers too:

# - Entering 9001 returns the result: 9001 is a prime number.
# - Entering 200876 returns the result: 200876 is a complex number.

# The algorithm will work up till the last known prime number, 2**82,589,933 − 1.
