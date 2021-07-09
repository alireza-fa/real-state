from abc import ABC


class Sell(ABC):
    def __init__(self, price_per_meter, discount=False, convertible=False,
                 *args, **kwargs):

        self.price_per_meter = price_per_meter
        self.discount = discount
        self.convertible = convertible
        super().__init__(*args, **kwargs)

    def show_price(self):
        return f'price :{self.price_per_meter}$\t' \
               f'discount :{self.discount}\t convertible :{self.convertible}\n'


class Rent(ABC):
    def __init__(self, initial_price, monthly_price, discount=False,
                 convertible=False, *args, **kwargs):

        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.discount = discount
        self.convertible = convertible
        super().__init__(*args, **kwargs)

    def show_price(self):
        return f'initial_price :{self.initial_price}$\t' \
               f'monthly_price :{self.monthly_price}$\t' \
               f'discount :{self.discount}\tconvertible :{self.convertible}\n'
