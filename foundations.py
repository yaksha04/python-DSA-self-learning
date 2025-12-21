###From here i am starting my python + DSA journey
print("hello world , I am yaksha")

x = 10          # int
y = 3.14        # float
name = "Python" # string
is_active = True # boolean

print(type(x), type(y), type(name), type(is_active))

a=19
b=27
add=a+b
print(add)

##name = input()
print(name ,"is unique")

##num=int(input("enter the num:"))
##multiply=num*10
##print(multiply)

for i in range(11):
    print(i)

## conditions check
##number=int(input("enter the number to check: "))
##if number%2==0:
    ##result='even'
##else:
    ##result='odd'   
##print(f"the {number} is {result}")    


list1=[1,2,3,4,5,6,76]
sum=0
for i in list1:
    sum =sum + i
print(sum)    
print("-------------------------")
for i in range(10):
    if i==7:
        break
print(f"here is 7 at index {i}")
print("-------------------------")   
cats=5
while cats > 0 :
    print(cats)
    cats=cats -1

print("-------------------------")
def add(a,b):
    return a+b
print(add(3,4))

print("-------------------------")

def greet(name):
    print(f"hello {name}")
print(greet("ramji"))    

print("-------------------------")

def check(num2):
    if num2%2==0:
        return True
    else:
        return False
x=check(3)
print(x)    

print("-------------------------")
def power(num1,pow=2):
    return num1**pow
print(power(10))
print(power(2,3))
print("-------------------------")

def add_all(*args):
    container=0
    for num in args:
        container=container+num
    return container
print(add_all(1,2,3,4,5,6,7,8,9,10))  
print("-------------------------")
def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
print(demo(1,2,3,4,age=20,name='yaksha'))    
print("-------------------------")
new= lambda x:x**4
print(new(4))

sosa=lambda a,b:a*b+10
print(sosa(2,4))
print("-------------------------")

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x+x-1, numbers))
print(squares)

print("-------------------------")
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 != 0, numbers))
print(evens)
print("-------------------------")
x = 10

def demo():
    x = 5
    print(x)

demo()
print(x)