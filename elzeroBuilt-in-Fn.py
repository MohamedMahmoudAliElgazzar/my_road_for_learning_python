# # # # # # ##########################
# # # # # # ##########69##############
# # # # # # ##########################

# # # # # # x=[1,2,3,4,[]]
# # # # # # if all(x):
# # # # # #     print('all elments is true')
# # # # # # else:
# # # # # #     print('there is at least one elment is false')
# # # # # # if any(x):
# # # # # #     print('there is at least one elment is true')
# # # # # # else:
# # # # # #     print('all elments is false')
# # # # # # print(bin(100))
# # # # # # a=1
# # # # # # b=2
# # # # # # print(id(a))
# # # # # # print(id(b))
# # # # # ##########################
# # # # # ##########70##############
# # # # # ##########################
# # # # # a=[1,10,19,40]
# # # # # print(sum(a))
# # # # # print(round(1.4581,2))
# # # # # #range(start,end,step)
# # # # # print(list(range(5,50,3)))
# # # # # print(list(range(20)))
# # # # # print('hello mohamed')
# # # # # print('hello', 'mohamed')
# # # # # print('hello', 'mohamed',sep='|')
# # # # # print('first line', end='\'')
# # # # # print('second line')
# # # # ##########################
# # # # ##########71##############
# # # # ##########################
# # # # # abs()
# # # # print(abs(15))
# # # # print(abs(-15))
# # # # print(abs(-415))
# # # # print(abs(415))
# # # # print('#'*44)
# # # # #pow() => power
# # # # print(pow(5,3))
# # # # print(pow(5,3,5))
# # # # print('#'*44)
# # # # #min()
# # # # mynumbers=(1,2,112,4,12,41,2,1)
# # # # print(min(15,5.4,541,5,4.45,5))
# # # # print(min(mynumbers))
# # # # print(max(mynumbers))
# # # # print('#'*44)
# # # # #slice()
# # # # a=['w','s','2','as']
# # # # print(a[slice(2)])
# # # ##########################
# # # ##########72##############
# # # ##########################
# # # #Map()
# # # def formatText(text):
# # #     return f"- {str(text).strip()} -"
# # # mytext=['osama','mohamed','mahmoud','ali']
# # # mtformated= map(formatText,mytext)
# # # print(mtformated)
# # # for name in mtformated:
# # #     print(name)
# # #     pass
# # # print('#'*44)

# # # for name in list (map(lambda text: f'- { str(text).strip().capitalize() } - ', mytext)) :
# # #     print(name,end =' - ')
# # #     pass
# # ##########################
# # ##########73##############
# # ##########################
# # #filter()

# # def checkNum(num):
# #     return num > 10
# # mynumbers=[1,2,321,41,5,235,12,3]
# # myResult=filter(checkNum,mynumbers)
# # for n in myResult:
# #     print(n)

# # print('#'*44)

# # def checkName(name):
# #     return str(name).startswith('O')
# # mynames=['Osama','Khaled','Omer','Omar','Ahmed','Osman']
# # myResult2=filter(checkName,mynames)
# # for n in myResult2:
# #     print(n)
# # print('#'*44)

# # myResult3=filter(lambda Name : str(Name).startswith('A'),mynames)
# # for n in myResult3:
# #     print(n)

# ##########################
# ##########74##############
# ##########################
# #Reduce()
# from functools import reduce
# def sumAll(*num):
#     return sum(list(*num))
# numbers=[12,3,14,12,412,31,2]
# print(sumAll(numbers))
# def sumAll2(num1,num2):
#     return num1+num2

# result=reduce(sumAll2, numbers) #(((12+3)+14)+12)...
# print(result)
# print('#'*44)
# print(reduce(lambda num1 , num2:num1+num2, numbers))
##########################
##########75##############
##########################
#enumerate(iterable,strat=0)
skills=["html",'plan1','plan2']
myskillCounter= enumerate(skills,start=100)
myskillCounter2= enumerate(skills,start=100)
for skill in skills:
    print(skill)

for counter, skill in myskillCounter:
    print(f'{counter} - {skill}')
for skill in myskillCounter2:
    print(skill)
print('#'*44)
mystring='elzero'
for letter in reversed(skills):
    print(letter)
