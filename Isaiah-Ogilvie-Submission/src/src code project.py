def is_prime(n):

	"""function defines a prime number."""

	if n <= 1:
		return f"{n} is not a prime number."
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return f"{n} is a complex number."
	return f"{n} is a prime number."

number = int(input("Enter a positive number: "))

"""variable number is defined as an integer based on input from user."""

print(is_prime(number))