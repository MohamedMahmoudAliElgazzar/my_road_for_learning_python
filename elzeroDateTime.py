# # ################################
# # ############79##################
# # ################################
# # # import datetime
# # # #print the current date and time
# # # print(datetime.datetime.now())
# # # print('#'*45)
# # # print(datetime.datetime.now().year)
# # # print(datetime.datetime.now().day)
# # # print(datetime.datetime.now().month)
# # # #print start and end of date
# # # print(datetime.datetime.min)
# # # print(datetime.datetime.max)
# # # print(datetime.datetime.now().time().hour)
# # # print(datetime.datetime.now().time().minute)
# # # print(datetime.datetime.now().time().second)

# # # print(datetime.time.min)
# # # print(datetime.time.max)
# # # print(datetime.datetime(2003,8,26))
# # # print(datetime.datetime(2003,8,26,))
# # # myBirthday=datetime.datetime(2003,8,26)
# # # datenow=datetime.datetime.now()
# # # print(f'I lived for {(datenow-myBirthday).days}')

# # ################################
# # ############80##################
# # ################################
# # #formate time
# # import datetime
# # myB=datetime.datetime(2003,8,26,20)
# # print(myB)
# # # print(myB.strftime('%B'))
# # # print(datetime.datetime)
# # #python's strftime directives
# # print(myB.strftime('%B'))
# # print(myB.strftime('%b'))
# # print(myB.strftime('%A'))
# # print(myB.strftime('%a'))
# # print(myB.strftime('%a / %b / %y'))

# # ###############################
# # ###########81##################
# # ###############################
# #iterator vs iterable
# #iterable = str list dic .. not int
# #iterator int boole float ...
# mystring= 'Mohamed'
# # for letter in mystring:
# #     print(letter,end="")
# iterTest=iter(mystring)
# # print(next(iterTest))
# # print(next(iterTest))
# # print(next(iterTest))
# # print(next(iterTest))
# # print(next(iterTest))
# # print(next(iterTest))
# # print(next(iterTest))
# for letter in iter('elzoer'):
#     print(letter,end=" ")
################################
############82##################
################################
def mygenerator():
    yield 1
    yield 2
    yield 3
    yield 4
print(mygenerator())
mygen=mygenerator()

# print(next(mygen)) 
# print('hello from python')
# print(next(mygen)) 
# print('hello from python')

# print(next(mygen)) 
# print('hello from python')

print(next(mygen)) 
for n in mygen:
    print(n)
    pass
