#question 1:
import math
class formula:
    def __init__(self,D):
       self.C = 50
       self.H = 30
       self.D = D
    def squareroot(self):
        Q=(2* self.C *self.D)/self.H
        z = math.sqrt(Q)
        return z  
x = formula(5)         
print(x.squareroot())

#question 2:
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print (aSquare.area())     

#Question 3:
class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

#question 4:
class Time():
    def __init__(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes
    def addTime(self,others):
        time3 = Time(0,0)
        if time1.minutes+time2.minutes > 60:
            time3.hours = int((time1.minutes + time2.minutes)/60)
        time3.hours = (time3.hours+time1.hours+time2.hours)
        time3.minutes = (time1.minutes + time2.minutes)- ((int((time1.minutes + time2.minutes)/60))*60)
        return time3

    def displayTime(self):
        print (self.hours,"hours and",self.minutes,"minutes.")
        return None

    def displayMinute(self):
        print ((self.hours*60)+self.minutes)      
        return None 

time1 = Time(2,50)
time2 = Time(1,20) 
c = Time.addTime(time1,time2)
c.displayTime()
c.displayMinute()

#question 5:
class person():
    def __init__(self, age):
        if age >= 0:
            self.age = age
        else:
            self.age = 0
            print('Age is not valid, setting age to 0')

    def yearPasses(self, value):
        self.age = self.age + value 

    def amIOld(self):   
        if self.age > 0 and self.age < 13:
            print('you are young')  
        elif 13 <= self.age <=19:
            print('You are a teenager')  
        else:
            print('you are old')         
    
age = person(8)
age.amIOld()
age.yearPasses(6)
age.amIOld()
age.yearPasses(10)
age.amIOld()


