class employee:
    __user_id=1
    def __init__(self):
        # Special method/Magic method/Dunder method/Constructor
        #print(id(self))
        self.__name="Default User"
        self.id=employee.__user_id
        employee.__user_id +=1
        self.salary=50000
        self.designation="SDE"

     # Method
    def travel(self,destination):
        print(f"Employee is travelling to {destination}")

    #Getter
    def get_name(self):
        return self.__name
    
    def set_name(self,value):
        self.__name=value

    # Static Method
    @staticmethod
    def get_id():
        return employee.__user_id
    
    @staticmethod
    def set_id(val):
        employee.__user_id=val


# Create an object/instance of class
sam = employee()

print(sam.id)
print(id(sam))
# Calling a method
print(sam.travel("Gujarat"))

print(type(sam))

### Accessing class from from module
#from OOPS_Proj import chatbook

#user1=chatbook()

## Encapsulation

# Access private attribute

print('Method 1',sam._employee__name) 


print('Method 2',sam.get_name())  # Getter Method

# Update private attribute
sam.set_name("Anil")    # Setter Method
print('Updated name',sam.get_name()) 


### Static Method
print('\n')
print('Static Method')

print('Sam id',sam.id)

James = employee()

print('James id',James.id)

# Using static method directly from class
employee.set_id(10)

Jack =employee()

print('Jack id',Jack.id)

