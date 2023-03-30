import random

UPPERCASE = list(range(65, 91))
LOWERCASE = list(range(97, 123))
NUMBERS = list(range(48, 58))
SPECIAL = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97))


def generate_password(length: int, uppercase: bool, lowercase: bool, numbers: bool, special: bool) -> str:
	password = ""
	characters = ""
	counter = 0
	compulsory = []

	if uppercase:
		for character in UPPERCASE:
			characters += chr(character)
		counter += 1
		compulsory.append(chr(random.choice(UPPERCASE)))

	if lowercase:
		for character in LOWERCASE:
			characters += chr(character)
		counter += 1
		compulsory.append(chr(random.choice(LOWERCASE)))

	if numbers:
		for character in NUMBERS:
			characters += chr(character)
		counter += 1
		compulsory.append(chr(random.choice(NUMBERS)))

	if special:
		for character in SPECIAL:
			characters += chr(character)
		counter += 1
		compulsory.append(chr(random.choice(NUMBERS)))

	if characters != "":
		random.shuffle(compulsory)

		for character in compulsory:
			password += character

		for i in range(0, length - counter):
			password += random.choice(characters)

		final = list(password)
		random.shuffle(final)

		password = ""

		for e in final:
			password += e

	return password


def write_file(line, file='data.txt'):
	f = open(file, 'a+')
	f.write(str(line) + '\n')
	f.close()


def read_file(file='data.txt'):
	f = open(file, 'r')

	lines = []

	for x in f:
		lines.append(x)

	return lines


def clear_file(file='data.txt'):
	f = open(file, 'w')
	f.close()
