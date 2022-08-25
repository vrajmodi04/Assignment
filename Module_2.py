#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Write a Python program to get the Factorial number of given number
n = int(input ("Enter a Number: "))
factorial = 1
if n >= 1:
    for i in range (1, n+1):
        factorial = factorial *i
    print ("Factorial of the given number is:", factorial)


# In[7]:


# Write a Python program to check if a number is positive, negative or zero
n = int(input("Enter any number: "))
if(n>0):
    print("positive number")
elif(n<0):
    print("negative number")
elif(n==0):
    print("number is zero")


# In[5]:


# Write a Python program to get the Fibonacci series of given range

n = int(input("how many terms:"))

n1, n2 = 0, 1
count = 0
if n <= 0:
    print("please enter a positive term.")
    
elif n == 1:
    print("Fibonacci sequence upto",n,":")
    print(n1)

else:
    print("Fibonacci sequence:")
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    


# In[15]:


# write a program to swap two number without using temp variable
a = 8
b = 9
a,b = b,a
print(a)
print(b)


# In[17]:


# write a program to swap two variable using temp variable
a=int(input("Enter a: "))
b=int(input("Enter b: "))
temp=0
temp=a
a=b
b=temp
print("a",a)
print("b",b)


# In[21]:


# Write a Python program to find whether a given number is even or odd,print out an appropriate message to the user

n=int(input("Enter any number: "))
if n%2==0:
    print("Given number is even.")
    print(n,"is even because it is divisble by 2 and the remainder is 0 therefore",n,"is even")
else:
    print("given number is odd.")
    print(n,"is odd because it is not divisble by 2 and the remainder is not 0 therefore",n,"is odd")


# In[26]:


# Write a Python program to test whether a passed letter is a vowel or not
n=input("Enter any character: ")

if n=='a' or n=='e' or n=='i' or n=='o' or n=='u':
    print("It is a vowel")
elif n=='A' or n=='E' or n=='I' or n=='O' or n=='U':
    print("It is vowel")
elif n.isnumeric:
    print("please enter a character")
else:
    print("It is not vowel")


# In[28]:


# Write a Python program to sum of three given integers.However, if two values are equal sum will be zero
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))
if a==b or b==c or a==c:
    print("0")
else:
    print(a+b+c)


# In[30]:


# Write a Python program that will return true if the two given integervalues are equal or their sum or difference is 5
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
if a==b or a+b==5 or a-b==5or-5:
    print("True")
else:
    print("False")


# In[33]:


#  Write a python program to sum of the first n positive integers
n=int(input("Enter a number: "))
sum=(n*(n+1))/2
print("the sum of ",n,"integer is: ",sum)


# In[3]:


#  Write a Python program to calculate the length of a string
s=input("Enter a string that you want to calculate the length: ")
print("the length of string is",len(s))


# In[4]:


# Write a Python program to count the number of characters (character frequency) in a string
s=input("Enter a string to count the number of characters : ")
c={}
for i in s:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print("count of all characters in s is :\n",str(c))


# In[8]:


# Write a Python program to count occurrences of a substring in a string
str1=input("Enter your string1: ")
str2=input("Enter your string2: ")
print(str1.count(str2))
print()


# In[6]:


# Write a Python program to count the occurrences of each word in a given sentence
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count(input('Enter your string: ')))


# In[2]:


# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string

a=input("Enter your string:")
b=input("Enter your string:")
x=a[0:2]
a= a.replace(a[0:2],b[0:2])
b= b.replace(b[0:2],x)


print('your first string has become: ',a)
print('your second string has become: ',b)


# In[4]:


#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' insteadif the string length of the given string is less than 3, leave it unchanged
x=input("enter a string: ")
if x.endswith('ing'):
    print(x.replace('ing','ly'))
elif len(x)>=3:
    print(x+"ing")
else:
    print(x)


# In[4]:


#  Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'substring with 'good'. Return the resulting string
def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1
print(not_poor(input("Enter your string:")))

