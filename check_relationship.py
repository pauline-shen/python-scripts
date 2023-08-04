f = open('matches.csv', 'r')
files = f.readlines()
f.close()
new_arr = []
for text in files:
	text = text.strip().split(", ")
	text[2], text[3] = eval(text[2].capitalize()), eval(text[3].capitalize())
	new_arr.append(text)

for i in range(len(new_arr)):
	r1 = new_arr[i]
	for j in range(len(new_arr)):
		if j == i: continue
		r2 = new_arr[j]
		if (r1[1] == r2[0] and r1[0] == r2[1]):
			print(j+1)