tries=4
pw="mohamed@123"
inputpw=input('write your password: ')
while inputpw != pw:
    tries -=1
    print( f'wrong pw, { "last" if tries ==0 else tries } chance left ')
    inputpw = input('write your password: ')
    if tries ==0:
        print('you have no more chanses')
        break
else:
    print('correct password!!')
print('loop is done')