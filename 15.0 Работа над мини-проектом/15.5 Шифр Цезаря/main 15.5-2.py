def forming_a_shift():
	org_text = str(input())
	list_org_text = org_text.split()
	list_total = []
	for i in range(len(list_org_text)):
		total = 0
		for j in range(len(list_org_text[i])):
			if list_org_text[i][j] not in ''' ! "#$%&’()*+,-./':;<=>?@[]^_`{|}~.''':
				total += 1
		list_total.append(total)

	return list_total, org_text


def classic_caesar_cipher(list_total, org_text):
	list_org_text = org_text.split()
	new_text = []
	for j in range(len(list_org_text)):
		word = list_org_text[j]
		range_number = list_total[j]
		new_word = ""
		for i in range(0, len(word)):
			letter_ord = ord(word[i])
			if 65 <= letter_ord <= 90:
				if letter_ord + range_number > 90:
					new_word += chr(((letter_ord + range_number) - 90) + 64)
				else:
					new_word += chr(letter_ord + range_number)
			elif 97 <= letter_ord <= 122:
				if letter_ord + range_number > 122:
					new_word += chr(((letter_ord + range_number) - 122) + 96)
				else:
					new_word += chr(letter_ord + range_number)
			else:
				new_word += word[i]


		new_text.append(new_word)
	return new_text


list_total, org_text = forming_a_shift()
print(*classic_caesar_cipher(list_total, org_text))
