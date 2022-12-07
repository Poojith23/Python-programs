#reverse the string

string=input("Enter string:")
rev=string.split()
rev.reverse()
print(' '.join(rev))



#even or odd check

num=int(input("Enter the number to check:"))
if(num%2)==0:
    print(num,"is an even number")
else:
    print(num,"is an odd number")
    


#Finding the cubes of given number

num=int(input("Enter the number:"))
for i in range(1,7):
    print("The current number is :",i,"The cube is ",i*i*i)



#To print multiplication table

num=int(input("Enter the number:"))
for i in range(20,0,-1):
    print(num,'x',i,'=',num*i)



#Multiply the numbers in a list

list=[4,2,3]
mul=1
for i in list:
    mul=mul*i
print(mul)
