num_1 = int(input("Please provide a number: "))
num_2 = int(input("What number do I divide by? "))
if num_1 % 4 == 0:
	print("Yooo!!!! Your Number is a multiple of 4 and divisible by 2")
elif num_1 % 2 == 0:
		print("Uuummm, your number is only divisible by 2.")
else:
	print("Hey!! Your number is not even!")


if num_2 % num_1 == 0:
	print("Hurray!! Your first and second number divide evenly!")
else:
	print("Ooops!! Your numbers don't divide evenly")