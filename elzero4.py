# a=0
# while a < 10:
#     a=a+1
#     print(a)
# else:
#     print("loop is done")

myf= ['mm','km','my','te','kh','me']
# print(len(myf))
a= 0
while a<len(myf):
    print(f'# { str( a + 1).zfill(2)} {myf[a]}')
    a = a+1
else:
    print("all friends printed to screen")
