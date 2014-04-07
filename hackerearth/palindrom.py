def palindrome(num):
    if num[::-1] == num:
       return True
    else:
       return False

t = int(raw_input())
for x in range(0, t):
    y = map(int, raw_input().split())
    flag = 0
    for z in range(int(y[0]), int(y[1]) + 1):
        if palindrome(str(z)) == True:
            flag += 1
    print flag