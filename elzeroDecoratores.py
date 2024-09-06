# # ##########################
# # ##########83##############
# # ##########################
# # #Decerator higher order Fn 
# # def myDecerator(Fn):#Decerator
# #     def nestedFn():
# #         print('before')
# #         Fn()
# #         print('after')
# #     return nestedFn
# # @myDecerator
# # def sayHello():
# #     print('Hello')
# # @myDecerator
# # def sayHi():
# #     print('hi')
# # # afterD=myDecerator(sayHello)
# # # afterD()
# # sayHello()
# # print('#'*50)
# # sayHi()
# ##########################
# ##########84##############
# ##########################
from time import time as tm
# def myDecerator(Fn):#Decerator
#     def nestedFn(n1,n2):
#         if n1<0 or n2<0:
#             print("there is a negative number")
#         print('before')
#         Fn(n1,n2)
#     return nestedFn

# def myDecerator2(Fn):#Decerator
#     def nestedFn():

#         print('coming from decerator 2')

#     return nestedFn
# @myDecerator
# @myDecerator2
# def calc(n1,n2):
#     print(n1+n2)
# calc(-5,20)
##########################
##########85##############
##########################
#
# def negativtyCheck(fn):
#     def NestedFn(*Numbers):
#         for number in Numbers:
#             if number < 0:
#                 print('there is At least one number that is negative')
#         fn(*Numbers)
#     return NestedFn
# # @negativtyCheck
# # def sum1(*numbers):
# #     i=0
# #     for num in numbers:
# #         i=i+num
# #     return i
# def sum1(num1,num2):

#     return num1+num2

# print(sum1(5,-8))
# mylist =[12,3124,12]
# i=0
# for num in mylist:
#     i=i+num
# print(i)
def speedTest(fn):
    def wrapper():
        start=tm()
        fn()
        end = tm()
        print(f'running time is : {end-start}')
    return wrapper
@speedTest
def biloop():
    for n in range(1,20000):
        print(n)
biloop()