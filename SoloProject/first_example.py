popitka = 0

for i in range(1_000_000_000, 8_999_999_999 + 1):

	total_zero_num = 0
	total_one_num = 0
	total_two_num = 0
	total_three_num = 0
	total_four_num = 0
	total_five_num = 0
	total_six_num = 0
	total_seven_num = 0
	total_eight_num = 0
	total_nine_num = 0
	total_rule = 0

	if "0" not in str(i):
		continue

	for a in range(0, len(str(i))):
		if str(i)[a] == "0":
			total_zero_num += 1

	for b in range(0, len(str(i))):
		if str(i)[b] == "1":
			total_one_num += 1

	for c in range(0, len(str(i))):
		if str(i)[c] == "2":
			total_two_num += 1

	for d in range(0, len(str(i))):
		if str(i)[d] == "3":
			total_three_num += 1

	for e in range(0, len(str(i))):
		if str(i)[e] == "4":
			total_four_num += 1

	for f in range(0, len(str(i))):
		if str(i)[f] == "5":
			total_five_num += 1

	for g in range(0, len(str(i))):
		if str(i)[g] == "6":
			total_six_num += 1

	for o in range(0, len(str(i))):
		if str(i)[o] == "7":
			total_seven_num += 1

	for v in range(0, len(str(i))):
		if str(i)[v] == "8":
			total_eight_num += 1

	for z in range(0, len(str(i))):
		if str(i)[z] == "9":
			total_nine_num += 1

	if str(i)[0] == str(total_zero_num):
		total_rule += 1

	if str(i)[1] == str(total_one_num):
		total_rule += 1

	if str(i)[2] == str(total_two_num):
		total_rule += 1

	if str(i)[3] == total_three_num:
		total_rule += 1

	if str(i)[4] == str(total_four_num):
		total_rule += 1

	if str(i)[5] == str(total_five_num):
		total_rule += 1

	if str(i)[6] == str(total_six_num):
		total_rule += 1

	if str(i)[7] == str(total_seven_num):
		total_rule += 1

	if str(i)[8] == str(total_eight_num):
		total_rule += 1

	if str(i)[9] == str(total_nine_num):
		total_rule += 1

	if total_rule == 9:
		print(i)
		print("МЫ НАШЛИ!")
		break

	# else:
	# 	total_num = 0
	# 	for bab in range(0,len(str(i))):
	# 		total_num += int(str(i)[bab])

		# if total_num == 10:
		# 	print(i)
		# 	print("МЫ НАШЛИ!")
		# 	break
	else:
		popitka += 1
		print(f"Попытка номер: '{popitka}'")


