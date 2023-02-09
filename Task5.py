#question 1:
x, y = input('Enter the number:').split(',')
try:
    z = x * y
    print(z)
except:
    print('syntax error')            
        
#question 2
import sys
file_name = sys.argv[1]
text = []
try:
    fh = open(file_name, 'r')
    text = fh.readlines()
    print(text)
except IOError:
    print('cannot open', file_name)
    print('Enter the correct file name')

#question 3:
x = input('enter 4 digit number:')
print(len(x))
if len(x) > 4:
    raise Exception('The length is too short/long !!! Please provide only four digits')


#question no :4
name = input('Enter username:')
password = input('Enter password:')
repass = input('Re_Enter password:')
x = 1
while x < 3:
    if password != repass:
        repass = input('Re_Enter password:')
        x += 1
    else:
        break 

#question no: 6
import sys
try:
    fh = open(sys.argv[1])
    for word in fh:
        string = word.split(' ') 
        if len(string)%2 == 0:
            print(string)
except:
    print('write file name properly')            
