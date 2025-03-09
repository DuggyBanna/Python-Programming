n=int(input("Enter the number of elements in the list: "))
l=[]
el=[]
ol=[]

for i in range(n):
    l.append(int(input("Enter the element: ")))
odd=0
even=0
for i in l:
    if i%2==0:
        el.append(i)
        even+=1
    else:
        ol.append(i)
        odd+=1
print("The list is: ",l)
print("Number of even numbers in the lis: ",el ,even)
print("Number of odd numbers in the list: ",ol,odd)
