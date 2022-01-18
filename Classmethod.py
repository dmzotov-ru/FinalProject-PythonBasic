class BaseCar:
    def __init__(self, **kwargs):
        self.car_type = kwargs['car_type']
        self.brand = kwargs['brand']
        self.carrying = kwargs['carrying']

    @classmethod
    def from_json(cls, cars):
        car_list = []
        for car in cars:
            print(car)
            car_list.append(cls(**car))
        return car_list


class Car(BaseCar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.passenger_seats_count = kwargs['passenger_seats_count']
        self.motor = kwargs['motor']


    def __repr__(self):
        return f"{self.brand}, {self.car_type}, {self.motor}. {self.carrying}, {self.passenger_seats_count}"


class Truck(BaseCar):
    def __init__(self,weight, height, lenght):
        super().__init__()
        self.weight = weight
        self.height = height
        self.lenght = lenght
        self.whl = self.weight * self.height * self.lenght


    def __repl__(self):
        return f"{self.brand}, {self.car_type}, {self.carrying}, {self.whl}"


y = Car({'brand': 'kia', 'car_type': 'car', 'carrying': 200, 'motor': 1.6, 'passenger_seats_count': 4})

