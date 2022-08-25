import sys

def fibo(number):
    if number > 1:
        return number * fibo(number-1)
    else:
        return 1
        

num = int(sys.stdin.readline())
print(fibo(num))