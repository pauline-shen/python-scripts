query = "insert into relationships (current_pet, other_pet, interact) values ({},{},{});\n"
f = open('matches.csv', 'r')
files = f.readlines()
f.close()
new = open('04_relationship.sql', 'w')
final = []
for text in files:
	text = text.strip().split(", ")
	text[2], text[3] = eval(text[2].capitalize()), eval(text[3].capitalize())
	if (text[2] and text[3]):
		final.append(query.format(text[0], text[1], 'true'))
		final.append(query.format(text[1], text[0], 'true'))
	elif (text[2] and not text[3]):
		final.append(query.format(text[0], text[1], 'true'))
new.writelines(final)
new.close()
