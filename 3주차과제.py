class car:
    car_count = 0

    def __init__(self, name, type, money):
        self.name = name
        self.type = type
        self.money = money
        car.car_count += 1


    def info(self):
        print(f'이름: {self.name}')
        print(f'차종 : {self.type}')
        print(f'금액 : {self.money}')


car1 = car('제네시스 G80' , '준대형' , '5300만원' )
car2 = car('테슬라 모델 S' , '준대형' , '1억 2천만원')


car1.info()
car2.info()



