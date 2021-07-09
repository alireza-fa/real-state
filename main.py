from sample import create_samples
from advertisement import ApartmentSell, ApartmentRent, HouseSell, HouseRent, \
    StoreSell, StoreRent


class Handler:
    ADVERTISEMENT_TYPES = {
        1: ApartmentSell, 2: ApartmentRent,
        3: HouseSell, 4: HouseRent,
        5: StoreSell, 6: StoreRent
    }

    CHOICE = {
        'r': 'get_report',
        's': 'show_all'
    }

    def get_report(self):
        for adv in self.ADVERTISEMENT_TYPES.values():
            print(adv, adv.manager.count())

    def show_all(self):
        for adv in self.ADVERTISEMENT_TYPES.values():
            print(adv, adv.show_detail)

    def run(self):
        for key, value in self.CHOICE.items():
            print(f'press {key}, for {value}')
        user_input = input('enter choice')
        switch = self.CHOICE.get(user_input, None)
        if switch is None:
            print('invalid choice')
            self.run()
        choice = getattr(self, switch, None)
        choice()
        self.run()


if __name__ == '__main__':
    create_samples()
    handler = Handler()
    handler.run()
