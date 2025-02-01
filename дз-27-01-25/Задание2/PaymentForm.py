from CreditCard import CreditCard

class PaymentForm():

    def __init__(self, card : CreditCard):
        self.__creditCard = card
    
    def pay(self, amount:float):
        return self.__creditCard.charge(amount)