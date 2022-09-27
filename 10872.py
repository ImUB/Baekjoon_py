def factorial(a):
	result = 1
	if a != 0:
		result = a * factorial(a-1)
	return result

N = int(input())

print(factorial(N))
