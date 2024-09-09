class Food:#base class


    def __init__(self,name,price) -> None:


        self.name=name


        self.price=price


        print(f'{self.name} is created from Food class')


        pass


    def eat(self):


        print('Eat method from super class')


class Apple(Food):#derived class


    def __init__(self,name,price,amount) -> None:


        # Food.__init__(self,name)


        super().__init__(name,price)


        # self.name=name


        self.amount=amount


        # self.price=price + 20


        print(f'{self.name} is created from apple class and price is {self.price} and the amount is {self.amount}')



        pass


    def get_from_tree(self):


        print('get from tree from derived class')



food1=Food("pizza",192)
food2=Apple('potato',140,11)
food2.eat()
food2.get_from_tree()

