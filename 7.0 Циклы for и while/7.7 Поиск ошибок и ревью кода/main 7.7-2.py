from math import pow

sum = 0
maxMin = int(-pow(10,6))

for _ in range(10):
    x = int(input())
    if x < 0:
        sum += x
    if maxMin < x < 0:
        maxMin = max(+x,+maxMin)

if sum == 0:
    print("NO")
else:
    print(sum, maxMin, sep="\n")

# mx = 0
# s = 0
# for i in range(11):
#     x = int(input())
#     if x < 0:
#         s = x
#     if x > mx:
#         mx = x
# print(s)
# print(mx)