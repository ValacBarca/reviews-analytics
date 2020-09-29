date = []
count = 0
with open ("reviews.txt", "r") as f:
	for line in f:
		date.append(line)
		count += 1
		if count % 1000 == 0:
		  print(len(date))


