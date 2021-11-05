list = [10, 1, 2, 20, 5, 8, 13, 21, 34, 4, 3]

for stuff in list:
	if stuff < 5:
		print(stuff)

num_in = int(input("Please provide a number: "))
for item in list:
	if item < num_in:
		print(str(item) + ", found in list is smaller than what you gave")
