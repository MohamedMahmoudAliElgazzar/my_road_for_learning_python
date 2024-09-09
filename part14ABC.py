from abc import ABCMeta , abstractmethod

class progr(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        return 'Yes!'
    
    pass



class python(progr):
    def has_oop(self):
        return 'Yes!'



class pascal(progr):
    def has_oop(self):
        return 'Not!'



one=pascal()
print(one.has_oop())