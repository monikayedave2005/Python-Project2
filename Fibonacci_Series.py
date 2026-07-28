# Fibonacci Series
no = int(input())
a = 0
b = 1
for _ in range(no):
    print(a, end=" ")
    a , b = b, a+b