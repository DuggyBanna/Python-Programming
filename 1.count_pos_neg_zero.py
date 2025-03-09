num=int(input("Enter the number of elements in the list:"))
input_list=[]
for i in range(num):
    input_list.append(int(input("Enter the element:")))

zero=0
pos=0
neg=0
for i in input_list:
    if(i==0):
        zero+=1
    elif(i>0):
        pos+=1 
    else:
        neg+=1
print("The list is:",input_list)
print("The number of positive numbers are:",pos)
print("The number of negative numbers are:",neg)
print("The number of zeros are:",zero)
