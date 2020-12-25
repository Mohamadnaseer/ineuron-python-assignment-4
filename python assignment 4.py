#!/usr/bin/env python
# coding: utf-8

# # python assignment 4

# 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below formula. area = (s(s-a)(s-b)(s-c)) * 0.5 Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass.

# In[78]:


class Shape:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.sides=[]
    def setsides(self):
        self.sides = [self.a,self.b,self.c]
        return self.sides
    a = int(input("Please enter the first side of a triangle:"))
    b = int(input("Please enter the second side of a triangle:"))
    c = int(input("Please enter the third side of a triangle: "))
class Triangle(Shape):
    def __init__(self,a,b,c):
        Shape.__init__(self,a,b,c)
        super(Triangle,self).__init__(a,b,c)
    def findArea(self):

        s = (self.a+self.b+self.c)/2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        try:
            print("The area of the triangle is %0.2f" %area)
        except:
            print("Incorrect entry - Not a Triangle ")
                  

t = triangle(a, b, c)
print(t.area())


# 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

# In[10]:


def filter_long_words(WordList,n):
    
    Wordlist=[x.strip() for x in WordList if len(x.strip())>n]
    
    if(len(Wordlist)>0):
        print("\n Output:")
        print("\n The List of longest words , which  are longer than "+str(n)+" is :")
        return Wordlist
    else:
        return "No Words longer than specified number "+str(n)
    
print("Input:")
string= input("Please enter your words: ")
number= int(input("Please enter your number: "))


list_Of_Words = list(string.split(","))

filter_long_words(list_Of_Words,number)


# 2.1 Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words. Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4] Here 2,3 and 4 are the lengths of the words in the list.

# In[3]:


def map_Words_to_Length(List):
    return list(map(len, List))

word_List=list(input("Input : Please enter Words : ").split(","))
List=[x.strip() for x in word_List]
Words_lengths=map_Words_to_Length(List)

print("Output: Length of Words are :",Words_lengths )


# 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
# it is a vowel, False otherwise.

# In[65]:


def identifyletter():
    print("Please type a letter")
    string=input()
    vowels='a','e','i','o','u'
    print("Is this letter a vowel?")
    for v in vowels:
        if v==string:
            print(True)
            break
    else:
        print(False)

identifyletter()

