#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
	number *= -1
	last_num = number % 10
	if last_num > 5:
		print(f"Last digit of {number * -1} is {last_num * -1} and is greater than 5")
	elif last_num < 6 and last_num != 0:
		print(f"Last digit of {number * -1} is {last_num * -1} and is less than 6 and not 0")
	else:
		print(f"Last digit of {number * -1} is {last_num} and is 0")
elif number > 0:
	last_num = number % 10
	if last_num > 5:
		print(f"Last digit of {number:d} is {last_num:d} and is greater than 5")
	elif last_num < 6 and last_num != 0:
		print(f"Last digit of {number:d} is {last_num:d} and is less than 6 and not 0")
	else:
		print(f"Last digit of {number:d} is {last_num} and is 0")
else:
	last_num = number % 10
	print(f"Last digit of {number:d} is {last_num} and is 0")
