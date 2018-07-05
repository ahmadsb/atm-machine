from datetime import date


class BankCard:

    def __init__(self, expiration_date,card_number,holder_name):
        self.expiration_date = expiration_date
        self.card_number = card_number
        self.holder_name = holder_name