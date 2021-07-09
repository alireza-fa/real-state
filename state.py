from abc import abstractmethod, ABC
from base import BaseClass


class BaseState(ABC):
    def __init__(self, area, rooms_count, build_year, address, user, region,
                 *args, **kwargs):

        self.area = area
        self.rooms_count = rooms_count
        self.build_year = build_year
        self.address = address
        self.user = user
        self.region = region
        super().__init__(*args, **kwargs)

    @abstractmethod
    def description(self):
        pass


class Apartment(BaseState):
    def __init__(self, floor, elevator=False, parking=False, *args, **kwargs):
        self.floor = floor
        self.elevator = elevator
        self.parking = parking
        super().__init__(*args, **kwargs)

    def description(self):
        return f'address :{self.address}\narea :{self.area}\t' \
               f'rooms_count :{self.rooms_count}\televator :{self.elevator}\t'\
               f'parking :{self.parking}\t build year :{self.build_year}\n' \
               f'seller detail :{self.user}'


class House(BaseState):
    def __init__(self, yard, floor_count, *args, **kwargs):
        self.yard = yard
        self.floor_count = floor_count
        super().__init__(*args, **kwargs)

    def description(self):
        return f'address :{self.address}\narea :{self.area}\t' \
               f'rooms count :{self.rooms_count}\tyard :{self.yard}\t' \
               f'floor count :{self.floor_count}\tbuild year :{self.build_year}\n' \
               f'seller detail :{self.user}'


class Store(BaseState):

    def description(self):
        return f'address :{self.address}\narea :{self.area}\t' \
               f'rooms_count :{self.rooms_count}\t' \
               f'build year :{self.build_year}\nseller detail :{self.user}'
