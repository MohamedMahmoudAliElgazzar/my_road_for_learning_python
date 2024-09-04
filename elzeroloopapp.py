# myrange= range(1,100)
# for num in myrange:
#     print(num)
myskills={
    "html" : '90%' ,
    "css" : '60%' ,

    "php": '70%',

    "js": '80%',
    "python": '90%'


}
# print(myskills['js'])
# print(myskills.get('python'))
for skill in myskills:
    # print(skill)
    print(f'my progress in lang {skill} is: {myskills[skill]}')
