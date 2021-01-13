from random import randint
from abc import abstractmethod, ABC


class RealtorMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class House:
    COST_OF_SQUARE_METER = 1000

    def __init__(self, area: int):
        self.area = area
        self.cost = self.area * self.COST_OF_SQUARE_METER

    def cost_with_discount(self) -> float:
        if self.area > 40:
            return self.cost
        else:
            return self.cost * 0.9


class Human(ABC):
    @abstractmethod
    def introduce(self):
        raise NotImplemented('You must to create method')

    @abstractmethod
    def make_money(self):
        raise NotImplemented('You must to create method')

    @abstractmethod
    def buy_a_house(self, realtor_for_deal, house):
        raise NotImplemented('You must to create method')


class Person(Human):
    def __init__(self, name: str, age: int, cash: int):
        self.__name = name
        self.__age = age
        self.cash = cash
        self.home = None

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    def introduce(self):
        print(f'My name is {self.name}, I am {self.age} years old.')

    def make_money(self):
        self.cash += 3000
        print(f"I work hard and I have {self.cash}$ now")

    def can_buy_house(self, cost: int) -> bool:
        return True if self.cash >= cost else False

    def buy_a_house(self, realtor_for_deal, desired_house: House) -> bool:
        deal = None
        money = self.cash
        if self.can_buy_house(desired_house.cost):
            deal = realtor_for_deal.deal(desired_house)
        if deal:
            print('I have a house!')
            return True
        elif not deal and self.cash == money:
            print("I will look for a house yet.")
        else:
            print(f"{realtor_for_deal.__name} steel my money!")
        return False


class Realtor(metaclass=RealtorMetaClass):
    def __init__(self, name: str, houses: list):
        self.__name = name
        self.houses_for_sale = houses
        self.__discount = 0.05

    @property
    def get_discount(self) -> float:
        return self.__discount

    def get_houses_info(self) -> list:
        print("Realtor: I have this houses for sale:")
        for house in self.houses_for_sale:
            print(f"{house.area} square meters for &{house.cost}. ")
        return self.houses_for_sale

    def deal(self, required_house: House, client, discount=False) -> bool:
        fair_play = randint(0, 9)
        if not fair_play:
            client.cash -= required_house.cost
            print('Realtor: ha-ha-ha! I steel your money!')
            return False
        else:
            for house in self.houses_for_sale:
                if house.area == required_house.area:
                    if discount:
                        cost = house.cost_with_discount() - (house.cost_with_discount()*self.get_discount)
                    else:
                        cost = house.cost
                    client.cash -= cost
                    client.home = house
                    self.houses_for_sale.remove(house)
                    print(f'Realtor: Deal is done!\n'
                          f'you now own a {house.area} square meter home that costs $ {cost}')
                    return True
        return False


if __name__ == '__main__':
    all_houses_areas = [40, 50, 60, 120, 33]
    houses_for_sale = [House(area) for area in all_houses_areas]

    man = Person('Rob', 42, 39000)
    realtor = Realtor('Joe', houses_for_sale)
    suitable_house = House(50)

    while not man.home:
        print('_' * 20)
        if suitable_house.area in (house.area for house in realtor.get_houses_info()):
            if man.can_buy_house(suitable_house.cost):
                new_house = realtor.deal(suitable_house, man, discount=True)
                if new_house:
                    print(f'System: {man.name} buy a house')
                else:
                    print("System: Rob hate realtors!")
                    break
            else:
                man.make_money()
        else:
            print("System: Realtor haven't required house")
            break
