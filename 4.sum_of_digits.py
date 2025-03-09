num=int(input("Enter a number: "))
temp=num
sum=0
while num>0:
    dig=num%10
    sum+=dig
    num=num//10
print("The sum of the digits is: ",temp,"is",sum)