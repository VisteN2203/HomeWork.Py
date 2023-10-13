def reform_num():
	global hex
	num = int(input())
	binary = bin(num)[2:]
	octal = oct(num)[2:]
	hex = hex(num)[2:]
	string_hex = str(hex).upper()
	return binary, octal, string_hex


print(*reform_num(), sep='\n')
