# class employee:
#     age:int
#     name:str
#     salary:float
#     marital_status:bool
    
#     def __init__(self,age) -> None:
#         print(self)
#         print(age)
#         self.age=age
#         # print(self.age)
    
#     def add(x,y)-> int:
#         return x+y    
    
    
# #emp=employee(10,'mayank',100.0,True) # emp is object refrence 
# emp=employee(10)
# print(emp.age)
# print(emp.add(10,20))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(squared_numbers)

import numpy
print(numpy.__version__)