from base import BaseClass


class User(BaseClass):
    def __init__(self, first_name, last_name, phone_number, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'Name ==> {self.first_name} {self.last_name}\t' \
               f'Phone Number ==> {self.phone_number}'
