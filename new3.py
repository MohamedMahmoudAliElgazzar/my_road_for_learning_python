import sqlite3
db=sqlite3.connect('app.db')
cr=db.cursor()
def commit_close():
    '''
    Commit Changes and Close Connection to Database
    '''
    db.commit()
    db.close()
    print('closed')

uid=1
input_message="""

's' => Show all skills
'a' => add new skill
'd' => Delete A skill
'u' => Update skill progress
'e' => Exit

Your Choice is : 
"""
choice= input(input_message).lower()
def show():
    cr.execute(f"select * from skills where user_id={uid}")
    result= cr.fetchall()
    print(f'you have {len(result)} Skills')
    print('Showing skills with progress: ')
    for row in result:
        print(f'Skill => {row[0]}',end=" ")
        print(f'Progress => {row[1]}%')
    commit_close()
    pass
def update():
    commit_close()
    pass
def delete():
    sk=input('Write Skill Name: ').strip().capitalize()
    cr.execute(f"delete from skills where name ='{sk}' and user_id='{uid}'")
    commit_close()
    print('Skill deleted succesfuly')
    pass
def add():
    sk=input('Write Skll Name: ').strip().capitalize()
    prog=input('write Skill progress [0-10] : ').strip()
    cr.execute(f"insert into skills(name, progress, user_id) values('{sk}','{prog}','{uid}')")
    commit_close()
    pass
def exit():
    commit_close()
    pass
if choice=='s':
    show()
    pass
elif choice=='a':
    add()
    pass
elif choice=='d':
    delete()
    pass
elif choice=='u':
    update()
    pass
elif choice=='e':
    exit()
    pass
else:

    print('Wrong input please try again!')
    db.close()


