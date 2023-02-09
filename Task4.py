# Question no:1
char = '1234abcd'
rev_char = char[len(char)-1::-1]
print(rev_char)

# Question no:2
def strin(char):
    uppercase = 0
    lowercase = 0
    #char = 'abcSdefPghijQkl'
    for i in char:
        if 97 <= ord(i) <= 122:
            lowercase += 1
            
        #return uppercase
        elif 65 <= ord(i) <= 90: 
            uppercase += 1
    return ('No. of uppercase character:{} No. of lowercase character:{}'.format(uppercase,lowercase))    
print(strin('abcSdefPghijQkl')) 

# Question no:3
def func(l):
    lis = list()
    for i in l:
        if i in lis:
            continue
        else:
            lis.append(i) 
    return lis           

print(func([1,3,4,2,5,6,3,2]))

# Question no:4
def sentence(char):
    lst = []
    char = char.split('-')
    char.sort()
    print('-'.join(char))
    return None
 
sentence(input('Enter the word with hypen:')) 


# Question no:5
def upper_case(sentence):
    uppercas = sentence.upper()
    print(uppercas)
    return None

upper_case(input('Enter the word:'))    


# Question no: 6
def sum1(x,y):
    x,y= int(x),int(y)
    z = x + y
    print(z)
    return None    

x, y = input("Enter multiple value: ").split(",")
sum1(x,y)


# Question no:7
def strin(x,y):
    if len(x) < len(y):
        print(y)
    elif len(x) > len(y):
        print(x) 
    else:
        print(x) 
        print(y)     

x,y = input('Enter the string:').split(',')
strin(x,y)


# Question no:8
def square(number):
    for i in number:
        z = tuple(i ** 2 for i in number)
        return z

y = (range(1,21,1))
print(square(y))

# Question no:9
def showNumbers(limit):
    x = limit
    for i in range(x + 1):

        if i % 2 == 0:
            print (i,' EVEN')
        else:
            print(i,' ODD')

showNumbers(3)

#Question No: 10
lis = range(1,21,1) 
even = list(filter(lambda x : x %2 == 0,lis))
print(even)

#question No: 11
numbers = range(1,10,1)
even = list(filter(lambda x : x %2 == 0,numbers))
square = list(map(lambda x : x ** 2, even))
print(square)

#question No: 12
try:
    x,y = 5,0
    print(x/y)
except ZeroDivisionError as error:
    print('Invalid')

#question No: 13
import functools

lis = [1,2,3,4,5]
word = functools.reduce(lambda x1,x2: str(x1) + str(x2),lis)
print(word)

#question no: 14
def printRange():
    num = range(1,100,1)
    for i in num:
        if i % 3 != 0 and i % 7 == 0:
            print(i)

def callRange(func):
    func()

callRange(printRange)

#question no: 15

def fun(n):
    return n * n
x = [1,2,3,4,5,6]
y = list(map(fun,x))
print(y)    


#question no:16

#(i) 2

# (ii) after f
        after f?
        Traceback
         a()
     NameError: name 'f' is not defined   





   
   

