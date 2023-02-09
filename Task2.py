# question 1
a = int(input('Enter the no'))
if (a % 3 == 0 and a % 5 == 0):
    print('Consultadd - Python Training')
elif (a % 5 == 0):
    print('Python training')
elif (a % 3 == 0):
    print('Consultadd')

# question 2
num = int(input('Enter the number from 1 to 5:'))
if type(num) == int:
    if num == 1:
        num1 = int(input('num1:'))
        num2 = int(input('num2:'))
        result = (num1+num2)
        print(result)
    elif num == 2:
        num1 = int(input('num1:'))
        num2 = int(input('num2:'))
        result =(num1-num2)
        print(result)
    elif num == 3:
        num1 = int(input('num1:'))
        num2 = int(input('num2:'))
        result =(num1*num2)
        print(result)
    elif num == 4:
        num1 = int(input('num1:'))
        num2 = int(input('num2:'))
        result = (num1/num2)
        print(result)
    elif num == 5:
        first = int(input('num1:'))
        second = int(input('num2:'))
        third = int(input('num3:'))
        fourth = int(input('num4:'))
        result = ((first + second + third + fourth)/4)
        print(result)
if result < 0:
    print('Negative')

#question 3
a = 10
b = 20
c = 30
avg = ((a+b+c)/3)
print('avg =', avg)
if (avg > a and avg > b and avg >c):
    print ('avg is higher than a,b,c') 
elif (avg > a and avg > b):
    print('avg is higher than a,b')
elif (avg > a and avg > c):
    print('avg is higher than a,c')
elif (avg > b and avg > c):
    print('avg is higher than b,c')
elif (avg > a):
    print('avg is just higher than a')  
elif (avg > b):
    print('avg is just higher than b')
else:
    print('avg is just higher than c')   

#question 4
num = int(input('Enter the number'))
while True:
    if num < 0:
        break
    if num > 0:
        print('good going')
print('It\'s over')

#question 5
for i in range(2000,3201,1):
    if i%7 == 0 and i % 5 != 0:
        print(i)

#question 6
1,'int' object is not iterable 

2, 0
   error
   1
   error
   2

3, NameError: name 'Break' is not defined


 #question 7
 for i in range(7):
    
    if i > 0 and i %3 == 0:
        continue
    else:
        print(i) 

#question 8
letter = input('enter the text:')
letters = 0
digits = 0
for i in letter:
    if ord(i) >= 97 and ord(i) <= 122 or ord(i) >= 65 and ord(i) <= 90:
        letters += 1
        
    elif ord(i) >= 48 and ord(i) <= 57:
        digits += 1
            
print('Letters', letters)
print('Digits', digits)    

#question 9
lucky_number = 6
while True:  
    guess_num =int(input('guess lucky_number from 0 to 9: '))
    if guess_num != 6:
        continue
    else:
        break
statement = 'you guessed correctly! The lucky number is {0}'
print(statement.format(lucky_number)) 

lucky_number = 6
while True:  
    guess_num =int(input('guess lucky_number from 0 to 9: '))
    if guess_num != 6:
        answer = input('Do you want to continue guessing? ')
        if answer == 'yes':
            continue
        if answer == 'no':
            print('better luck next time!')
            break
    else:
        statement = 'you guessed correctly! The lucky number is {0}'
        print(statement.format(lucky_number))
        break

#question 10
lucky_number = 6
counter = 1
while counter <= 5:
    guess_number = int(input('Type in the nmber'))
    counter = counter + 1
    if guess_number == lucky_number:
        print('good guess!')
    else:
        if counter < 6:
            print('try again.')
print('Game over!') 

#question 11
lucky_number = 6
counter = 1
while counter <= 5:
    guess_number = int(input('Type in the nmber'))
    counter = counter + 1
    if guess_number == lucky_number:
        print('good guess!')
        break
   
if counter == 6:
    print('Sorry that was not very success at all!') 

    