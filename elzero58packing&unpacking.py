# # print(1,2,3,4,5)
# # def hello(*ppl):
# #     for name in ppl:
# #         print(f'Hello {name}')
# # hello('h','m','o')
# # def showDetails(name, *skill):
# #     print(f'hello {name} ! your skills are: ')
# #     for s in skill:
# #         print(f' - {s}')
# # showDetails('mohamed','python','datascience','SOC')
# # #######################
# # #######video 60########
# # #######################
# def showSkills(**skill):
#     print(type(skill))



#     for skills, value in skill.items():

#         print(f'{skills} => {value}')




#     pass
# showSkills(Js='39%',XDR='41%',CTF='23%',IAC='14%')
# # showSkills(**dictonary)
# #######################
# #######video 61########
# #######################


def showSkills(name,*skills,**skillsP):
    print(f'Hello {name} \nyour skills that have no progress are: ')
    for skill in skills:print(f'- {skill}')
    print('and your skills that have progress are : ')
    for skill,value in skillsP.items():
        print(f'- {skill} => {value}')


        pass

    pass
mytuple=('fast typing','social engineering','runner')
name ='mohamed'
showSkills(name,*mytuple,**myskill)




























