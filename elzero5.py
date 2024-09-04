myfavwebs=[]
maxwebs=5
while maxwebs>0:
    web= input('website name: ')
    myfavwebs.append(f'https://{web.strip().lower()}')
    maxwebs -=1
    print(f'website added, {maxwebs}places left')
    print(myfavwebs)
else:
    print('you have reached the max websites')
if len(myfavwebs)>0:
    myfavwebs.sort()
    index=0
    print('the list of website: \n')
    while index< len(myfavwebs):
        print(myfavwebs[index])
        index +=1
          