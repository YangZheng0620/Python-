def collatz(number):
	if number % 2 == 0:
		return number // 2
	elif number % 2 == 1:
		return 3 * number + 1
	else:
		print('Error')

try:
	num = int(input('Enter number:'))
	while num != 1:
		print(collatz(num))
		num = collatz(num)
except ValueError:
	print('valueError')

	

