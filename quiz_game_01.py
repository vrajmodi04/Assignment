#!/usr/bin/env python
# coding: utf-8

# In[9]:


Question = []
Option = []
Right_Answer = []
print('Type 1 to select master role'.center(90))
print('Type 2 to select cracker role'.center(90))
print('Type 3 to exit the game'.center(90))
while True:
    a = int(input('Please Type 1 or 2 to continue: '))
    if a==1:
        print('Welcome Master'.center(100),'\n',
            'Menu'.center(70),'\n',
            'press 1 to add Questions','\n',
            'press 2 to view Questions','\n',
            'press 3 to delete Question','\n',
            'press 4 to exit')
        while True:
            n=int(input("select operation which you want to perform: "))
            if n==1:
                que = input('Enter Question: ')
                f = int(input('How many option you want: '))
                op=[]
                for i in range(int(f)):
                    d = input("op" + str(i+1) + ": ")
                    op.append(d)
                ra = input("Right Answer: ")
                Question.append(que)
                Option.append(op)
                Right_Answer.append(ra)
            elif n==2:
                for i in range(len(Question)):
                    print("Question" + str(i+1) + ": " + str(Question[i]))
                    print("Option : " + str(Option[i]))
                    print("Right answer : " + str(Right_Answer[i]))
            elif n==3:
                Question.pop(0)
                Option.pop(0)
                Right_Answer.pop(0)
            elif n==4:
                print('Exit')
                break
            else:
                break
                print('select from 1 to 4 only')
    elif a==2:
        print('welcome cracker'.center(90))
        r=0
        w=0
        for i in range(len(Question)):
            print(Question[i])
            print(Option[i])
            z=input('Enter your answer: ')
            if z in Right_Answer:
                print("Correct")
                r=r+1
            else:
                print("Incorrect")
                w=w+1
        print("Your True Answer = " + str(r))
        print("Your Wrong Answer = " + str(w))
        break
    elif a == 3:
        print("Exit")
        break
    else:
        print("Enter a valid number")

