# Polymorphism
def f(x,y):
    print("values: ", x, y)

f([3,5,6],(3,5))

f("A String", ("A tuple", "with Strings"))

f({2,3,9}, {"a":3.4,"b":7.8, "c":9.04})

#### Method Overloading
class Human:

    def sayHello(self, name=None):
    
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
        

# Create instance
obj = Human()
    
# Call the method
obj.sayHello()
    
# Call the method with a parameter
obj.sayHello('Gav')


### Operator Overloading
print(4 + 4) # Addition
print('He' + 'llo') # Concatenation


### Method Overriding
class Parent(): 
        
    def __init__(self): 
        self.value = "Parent's __init__"
          
    def show(self): 
        print(self.value) 
          
# Define child class 
class Child(Parent): 
        
    def __init__(self): 
        self.value = "Child's __init__"
          
    # Same method name as parent class
    def show(self): 
        print(self.value) 
          
          

obj1 = Parent() # Parent's __init__
obj2 = Child() # Child's __init__
  
obj1.show() 
obj2.show()


### Method Overloading
def x(a):
    return a

# Same function name different signature
def x(y, z): 
    return y + z

print(x(1)) # TypeError
# print(x(2,3)) # 5