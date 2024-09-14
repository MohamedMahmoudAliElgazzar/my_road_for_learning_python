# n=int(input())
n=5
# x=input()
x='5 4 3'
x_levels=x.split(' ')
# y=input()
y='1 2 3'
y_levels=y.split(' ')
n_levels=[]
x1_levels=[]
y1_levels=[]
for ite1 in x_levels:
    x1_levels.append(int(ite1))
for ite2 in y_levels:
    y1_levels.append(int(ite2))
while n>0:
    n_levels.append(n)
    n-=1
for n1 in n_levels:
    if n1 in x1_levels or n1 in y1_levels:
        n_levels.remove(n1)
        continue
    else:
        print('oh my keyboard')
        break
if len(n_levels)==0:
    print('oh my boy')

print(n_levels)
print(x1_levels)
print(y1_levels)
