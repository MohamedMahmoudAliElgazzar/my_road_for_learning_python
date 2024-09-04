admins=[ "ahmed","osama",'samed','manal','rahma', 'mahmoud','enas']

name =input("please enter your name: ").strip().lower()

if name in admins:
    print(f"hello {name} welcome back")
    option= input('delete or update your name? [u,d]').strip().lower()
    print(option)
    if option =='u':
        theNewName = input("enter your new name please: ").strip().lower
        admins[admins.index(name)]= theNewName
        print(f"name updated")
    elif option =='d':
        admins.remove(name)
        print("you're no longer an admin!")
    else :
        print("this is wrong option, try again please!")
        
else:
    status = input("Not Admin, sing in? [Y,N]").strip().lower()
    if status =='y':
        print(' you have been added')
        admins.append(name)
        print(admins)
    else:
        print('Nice to meet you!')