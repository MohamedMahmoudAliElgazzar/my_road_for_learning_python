
x=input()
my_list=list(x)
result=0

i=0
j=1
while i< len(my_list):
    if i==len(my_list)-1:
        result+=1
        break
    elif my_list[i]== my_list[j]:
        i+=1
        j=i+1
    else:
        j+=1
        if j==len(my_list) :
            i+=1
            j=i+1

            result+=1
if result%2==0:print('CHAT WITH HER!')
else:print('IGNORE HIM!')

