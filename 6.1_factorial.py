def factorial(n):
    if(n==1):
        return 1
    return n*factorial(n-1)
n=int(input("Enter the number: "))
if(n<0):
    print("Factorial of negative number is not possible")
elif(n==0):
    print("Factorial of 0 is 1")
else:
    print("Factorial of",n,"is",factorial(n))