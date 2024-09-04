# ppl=['o','p','c','s']
# skills=['html','css','js']
# for name in ppl:
#     print(f'{name} skills is: ')
#     for skill in skills:
#         print(f'- {skill}')
ppl={
    'o': {
        'html':'70%',
        'css' :'80%',
        'js' : '90'

    },
    'a':{
        'html':'90%',
        'css' :'80%',
        'js' : '90'

    },
    's':{
        'html':'70%',
        'css' :'60%',
        'js' : '90'

    }

}
# print(f'{ppl["o"]}')
# print(ppl["o"]["css"])
for name in ppl:
    print(f'skills and progress for {name} is: ')
    for skill in ppl[name]:
        print(f'{skill.upper()} => {ppl[name][skill]}')