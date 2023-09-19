# x=10
# y=20
# print(float(x))
# print(float(y))
# print(complex(y))
# print(complex(x))
# print(int(x))


# a=5
# b=6

# a+=5
# b-=5
# print(a)
# print(b)

# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)

# a,b=b,a
# print(a,b)

# if(10<11):
#   print("greater")




#if(6>5):
#       print("greater")
#else:
#       print("smaller")


 
# ?)find greater number the 3 digits given by the user?
# a=int(input("enter the first value"))
# b=int(input("enter the second value"))
# c=int(input("enter the 3rd value"))    
# if(a>b):
#     if(a>c):
#         print("first value is greater")
#     else:
#          print("3rd value is greater")
# elif(b>c):
#     print("second value is greater")
# else:
#     print("3rd value is greater") 



# ?)check whether the given number is even or odd?
# a=int(input("enter the value"))
# if(a%2==0):
#    print("number is odd")
# else:
#    print("number is even")



# ?)leap year?
# a=int(input("enter year"))
# if(a%4==0):
#     print("is a leap year")
# else:
#     print("is not a leap year")



# ?)tuple
# t=(1,2,3,4,5,"hai")
# y=list(t)
# y[5]="hello"
# t=tuple(y)
# print(t)   



# ?)list
# list1=[1,2,9,4,5,6,7]
# list1[3]=3
# print(list1)



# ?)set
# s={1,2,3,4,5,"hai"}
# y=list(s)
# y[3]="hello"
# s=set(y)
# print(s)


# ?) WAP to check whether the last digit of a number is divisible by 3 or not?
# a=int(input("enter a number"))
# if(a%3!=1):
#   print("number is divisible by 3")
# else:
#   print("numbe not divisible by 3") 


   
# ?)display "HELLO" if entered number is divisible by 5 otherwise print bye
# a=int(input("enter number"))
# if(a%5!=1):
#   print("HELLO")
# else:
#   print("Bye") 



# ?)to accept percentage from the user and display the grade according following criteria
# n=int(input("enter mark"))
# if(n>90):
#   print("A grade")
# elif(n>80 and n<=90):
#   print("B grade")
# elif(n>=60 and n<=80):
#   print("C grade")
# elif(n<60):
#   print("D grade")  



# ?)wirte a program to display the last digits of a number.
# a=int(input("enter a number"))
# x=a%10
# print("the last digits is",x)


# ?) calculate electricity bill.
# a=int(input("enter the unit of electricity"))
# if(a<100):
#     print("no charge")
# elif(a>100 and a<=200):
#     x=(a-100)*5
#     print("electricity bill",x)
# elif(a>200):
#     x=500+(a-200)*10
#     print("electricity bill",x)
    





# ?)Write a program that takes a list of strings as input and outputs the length of each string using a while loop.
# n=int(input("Enter limit"))
# i=1
# list=[]
# count=[]
# while(i>=0 and i<=n):
#     a=input("enter the string")
#     list.append(a)
#     b=len(a)
#     count.append(b)
#     i=i+1 
# print(list)
# print(count)    



# ?)Write a program that takes a string as input and outputs the number of times each character appears in the string using a while loop.    
# string=input("Enter string")
# print(string)
# char=input("Enter charecter to be counted")
# i=0
# count=0
# while(i<len(string)):
#     if(string[i]==char):
#         count=count+1
#     i=i+1 
# print("Number of charecter appered is",count)    


# ?)Write a program that takes two lists of integers as input and returns a list containing the common elements using a while loop.
# n=int(input("Enter the first limit"))
# i=1
# list1=[]
# list2=[]
# result=[]
# while(i>=0 and i<=n):
#     a=int(input("Enter the integers"))
#     list1.append(a)
#     i=i+1
# m=int(input("Enter the second limit"))
# j=1
# while(j>=0 and j<=m):
#     b=int(input("Enter the integers"))
#     list2.append(b)
#     j=j+1
# k=0
# while(k<len(list1)):
#     if(list1[k] in list2):
#         result.append(list1[k])
#         k=k+1
#     print(list1)
#     print(list2)
#     print(result)          


# ?)Write a program that takes a string as input and outputs the string in reverse order using a while loop.
# n=int(input("Enter a string"))
# reverse=0
# while(n!=0):
#     x=n%10
#     reverse=reverse*10+x
#     n//=10
# print(reverse)    

# ?)Write a program that takes a list of integers as input and outputs the sum of the integers using a while loop.
# n=int(input("Enter the value:"))
# sum=0
# while(n>=0):
#     sum+=n
#     n-=1
    
# print("sum is",sum)