#assignment question.6 
n = int(input())
for _ in range(n):
    a, b = input().split()
    a = int(a[::-1])
    b = int(b[::-1]) 
    s = a + b
    print(str(s)[::-1].lstrip('0'))