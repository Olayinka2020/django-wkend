data = input("Enter words: ")
spot = []
for item in data:
	if item in spot:
		print("not isogram")
		break
	else:
		spot.append(item)