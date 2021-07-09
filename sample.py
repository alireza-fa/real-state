from region import Region
from random import choice
from user import User
from advertisement import ApartmentSell, ApartmentRent, HouseSell, HouseRent, \
    StoreSell, StoreRent

FIRST_NAME = ['alireza', 'mamad', 'hossein', 'amir']
LAST_NAME = ['faizi', 'shirzad', 'hosseini', 'shahi']
NUMBERS = ['09306664585', '091231331225', '+165854575', '09121456585']

for number in NUMBERS:
    User(choice(FIRST_NAME), choice(LAST_NAME), number)

reg1 = Region(name='canada')


def create_samples():

    apartment_sell = ApartmentSell(
        floor=3, elevator=True, parking=True, area=100, rooms_count=2,
        build_year=2019, address='ottawa', user=User.objects_list[1],
        region=reg1, price_per_meter=1000, discount=True,
        convertible=True
    )

    apartment_sell2 = ApartmentSell(
        floor=4, elevator=True, parking=True, area=200, rooms_count=4,
        build_year=2019, address='ottawa', user=User.objects_list[3],
        region=reg1, price_per_meter=2000
    )

    apartment_rent = ApartmentRent(
        floor=3, elevator=True, parking=True, area=200, rooms_count=2,
        build_year=2019, address='ottawa', user=User.objects_list[3],
        region=reg1, initial_price=16000, monthly_price=2000, discount=True,
        convertible=True
    )

    apartment_rent2 = ApartmentRent(
        floor=3, elevator=True, parking=True, area=220, rooms_count=3,
        build_year=2019, address='ottawa', user=User.objects_list[2],
        region=reg1, initial_price=16000, monthly_price=2000
    )

    house_sell = HouseSell(
        yard=True, floor_count=1, area=200, rooms_count=3,
        build_year=2013, address='ottawa', user=User.objects_list[1],
        region=reg1, price_per_meter=2000, discount=True, convertible=True
    )

    house_sell2 = HouseSell(
        yard=True, floor_count=2, area=300, rooms_count=6,
        build_year=2018, address='ottawa', user=User.objects_list[0],
        region=reg1, price_per_meter=2000
    )

    house_rent = HouseRent(
        yard=True, floor_count=2, area=300, rooms_count=6,
        build_year=2018, address='ottawa', user=User.objects_list[3],
        region=reg1, initial_price=10000, monthly_price=3000,
        discount=True, convertible=False
    )

    house_rent2 = HouseRent(
        yard=True, floor_count=2, area=250, rooms_count=4,
        build_year=2018, address='ottawa', user=User.objects_list[0],
        region=reg1, initial_price=10000, monthly_price=2000,
    )

    store_sell = StoreSell(
        area=40, rooms_count=0, build_year=2001, address='ottawa',
        user=User.objects_list[3], region=reg1, price_per_meter=2000,
        discount=True, convertible=True
    )

    store_sell2 = StoreSell(
        area=50, rooms_count=0, build_year=2001, address='ottawa',
        user=User.objects_list[1], region=reg1, price_per_meter=2500,
    )

    store_rent = StoreRent(
        area=110, rooms_count=2, build_year=2001, address='ottawa',
        user=User.objects_list[0], region=reg1, initial_price=0,
        monthly_price=3000, discount=False, convertible=True
    )

    store_rent2 = StoreRent(
        area=120, rooms_count=1, build_year=2001, address='ottawa',
        user=User.objects_list[2], region=reg1, initial_price=0,
        monthly_price=3000
    )

    print('#' * 20, '\tcreate sample\t', '#' * 20)
