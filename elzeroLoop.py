 

# myskills={
#     'html':'70%',
#     'css' :'80%',
#     'js' : '90',
#     'php': '80%'
# }
# for skill in myskills:
#     print(f'{skill} => {myskills[skill]}')

# for key,progress in myskills.items():
#     print(f'{key}=> {progress}')
myskills ={
    'html':{
        'main': '90',
        'sass':'60%'
        },

    'css' :{
        'main': '40',
        'sass':'20%'
        }
}
print(myskills.items())
print('#'*50)
for mKey,mValue in myskills.items():
    print(f'{mKey} progress is : ')
    for ckey,cvalue in mValue.items():
        print(f'{ckey}=> {cvalue}')
