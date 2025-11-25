
n = int(input("Enter number of terms (n): "))

if n <= 0:
	print("Please enter a positive integer.")
else:
	a, b = 0, 1
	for i in range(n):
		# print current term with a space separator
		if i < n - 1:
			print(a, end=' ')
		else:
			print(a)
		a, b = b, a + b

