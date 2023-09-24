m, n = int(input()), int(input())

# for i in range(m, n, -2):
#     if i % 2 != 0:
#         print(i)
#     else:
#         print(i - 1)

for i in range(m, n, -2):
    a = (i % 2) - 1
    print(i + a)
