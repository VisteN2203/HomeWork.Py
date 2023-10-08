def sorted_list(num):
	new_list = []
	num -= 1
	while num != -1:
		use_list = main_list[num]
		new_list += use_list
		new_list.sort()
		num -= 1
	return new_list


number_of_list = int(input())
main_list = []


def creating_list(num, use_list):
	for i in range(num):
		list = [int(c) for c in input().split()]
		use_list.append(list)


creating_list(number_of_list, main_list)
print(*sorted_list(number_of_list))
