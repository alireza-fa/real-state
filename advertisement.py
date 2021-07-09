from base import BaseClass
from state import Apartment, House, Store
from deal import Sell, Rent


class ApartmentSell(BaseClass, Apartment, Sell):

    def show_detail(self):
        print(f'Apartment Sell :{self.id}')
        print(self.description())
        print(self.show_price())


class ApartmentRent(BaseClass, Apartment, Rent):

    def show_detail(self):
        print(f'Apartment Rent :{self.id}')
        print(self.description())
        print(self.show_price())


class HouseSell(BaseClass, House, Sell):

    def show_detail(self):
        print(f'House Sell :{self.id}')
        print(self.description())
        print(self.show_price())


class HouseRent(BaseClass, House, Rent):

    def show_detail(self):
        print(f'House Rent :{self.id}')
        print(self.description())
        print(self.show_price())


class StoreSell(BaseClass, Store, Sell):

    def show_detail(self):
        print(f'Store Sell :{self.id}')
        print(self.description())
        print(self.show_price())


class StoreRent(BaseClass, Store, Rent):

    def show_detail(self):
        print(f'House Rent :{self.id}')
        print(self.description())
        print(self.show_price())
