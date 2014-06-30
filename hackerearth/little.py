t = int(raw_input())
for x in range(0, t):
    count = 0
    y = map(int, raw_input().split())
    z = int(raw_input())
    sum = int(y[0])
    while sum%z != 0:
        sum = sum + int(y[1])
        count = count + 1
    print count
