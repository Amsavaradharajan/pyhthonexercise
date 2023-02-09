#question 1
lis = [1,2.3,'hello',2+3j,3+5j,5.7,9.2,'python',4,6]
for i in lis:
    print(i)

#question 2
lis = [1,2,3,4,5]
slic = lis[1:3:1]
print (slic)

#question 3
lis = [1,2,3,4,5,6]
sum1 = sum(lis)
print(sum1)
tem = 1
for num in lis:
    tem = tem * num
print(tem)    

#question 4
numbers = [1, 2, 3, 5, 9, 6, 100, 82, 63, 6, 101,5]
maximu = numbers[0]
for i in numbers:
    if i > maximu:
        maximu = i
print("Largest number is: ", maximu)

list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Smallest number is:", list1[0])

#question 5
num = [7,8, 120, 25, 44, 20, 27]
num = [x for x in num if x%2!=0]
print(num)

#question 6
lis = list()
for x in range(31):
    if x == 0:
        continue
    if x == 1 or x <=25: 
        y = x
        lis.append(y)
    else:
        y = x**2
        lis.append(y)
print(lis) 

#question 7
num1 = [1,3,5,7,9,10]
num2 = [2,4,6,8]
num1.pop(-1)
num1.extend(num2)
print(num1)

#question 8
a={1:10,2:20}
b={3:30,4:40}
c ={}
for d in (a,b) :
  c.update(d)
print(c)

#question 9
n = 5
dic1 = {}
for x in range(1,n + 1):
    dic1[x] = x * x
print(dic1)

#question 10
stri = input('enter the comma separated value')
splited = stri.split(',')
tup = tuple(splited)
#print('{}{}'.format(splited,tup))
print(splited,tup)