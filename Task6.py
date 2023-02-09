string ='AMSA'
result = [ x.isupper() for x in string]

print(result)

students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
x = zip (students,subjects)
print(dict(x))

str = ''
def reverse_string(my_str):
    length = len(my_str)
    for i in range(length-1, -1, -1):
        yield my_str[i]


for char in reverse_string('Consultadd Training'):
    str = str + char
print(str)    


#question no:5
def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()
   
