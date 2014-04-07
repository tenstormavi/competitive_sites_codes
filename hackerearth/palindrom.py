t = int(raw_input())
num = raw_input()
sam = num.split()
flag = 0
for i in range(int(sam[0]), int(sam[1]) + 1):
	if str(i) == str(i)[::-1]:
		flag = flag + 1
print flag
