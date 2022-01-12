#recursive rogram to find fibonacci series
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
x=int(input("ENTER A NUMBER"))
print(fib(x))