# class member:
#     def __init__(self,name) -> None:
#         print('')
#         self.name=name

# one=member('AHMED MOHSEN')
# one.name='sayed'
# print(one.name)
class member:
    def __init__(self,name,age) -> None:
        
        self.__name=name
        
        self.__age=age
        ########
#______________________

    def say_hello(self):
        


        print(f'hello {self.__name}')
        ########
#______________________

    def get_name(self):#Getter
        

        return self.__name
        ########
#______________________

    def set_name(self,new_name):
        
        self.__name=new_name
        ########
#______________________

    def get_age(self):#Getter
        

        return self.__name
        ########
#______________________

    def set_age(self,new_age):
        
        self.__age=new_age
        ########
#______________________

    @property
    def age_in_days(self):
        
        return self.__age*12*30
        ########
#_____________________________________

    

    

one=member('AHMED MOHSEN',12)
# print(one.__name)
# one.__name='sayed'
one.say_hello()

# print(one.__name)
#you supposed to not access the __name because it is privet but unfortiently there is a way to acces it 
# and this is the way:
print(one._member__name)
# but you can say that __  is just a way to tell the developers that this is your rule 
# there is no restricion 
print(one.get_name())
one.set_name('Mohamed Mohsen')
print(one.get_name())
one.set_age(21)
print(one.get_age())
print(one.age_in_days)