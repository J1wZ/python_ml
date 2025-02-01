from datetime import date

class CreditCard:

    def __init__(self, cardNumber = "1234567891234567", cardHolder = "Иван Иванович", expiryDate = date(1,1,1), cvv = '123', money = 0.0):
        if CreditCard.checkCardHolder(cardHolder) and CreditCard.checkCardNumber(cardNumber) and CreditCard.checkCvv(cvv) and CreditCard.checkExpiryDate(expiryDate) and CreditCard.checkMoney(money):
            self.__cardNumber = str(cardNumber)
            self.__cardHolder = cardHolder
            self.__expiryDate = expiryDate
            self.__cvv = str(cvv)
            self.__money = float(money)
        else:
            raise Exception("Ощибка при введении данных")
    
    def getCardNumber(self):
        return self.__cardNumber
    
    def getCardHolder(self):
        return self.__cardHolder
    
    def getExpiryDate(self):
        return self.__expiryDate
    
    def getCvv(self):
        return self.__cvv
    
    def charge(self, amount:float):
        if isinstance(amount, float):
            if (amount >= 0.0):
                if amount > self.__money :
                    raise Exception(f"Не достаточно денег на карте.\nБаланс карты: {self.__money}")
                else:
                    self.__money -= amount
                    result = f"Успешно списано {amount}\nБаланс карты: {self.__money}"
                    return result
            else:
                raise Exception(f"Вы ввели отрицательное число")
        else:
            raise Exception(f"Можно вводить только неотрицательные числа.")
    

    def checkCardNumber(cardNumber):
        cardNumber = str(cardNumber)
        if len(cardNumber) == 16 and cardNumber.isnumeric():
            return True
        return False

    def checkCardHolder(cardHolder):
        if isinstance(cardHolder, str) and not cardHolder.isdigit() and cardHolder.count(' ') == 1:
            return True
        return False
    
    def checkExpiryDate(expiryDate):
        if isinstance(expiryDate, date):
            return True
        return False
    
    def checkCvv(cvv):
        cvv = str(cvv)
        if len(cvv) == 3 and cvv.isnumeric():
            return True
        return False
    
    def checkMoney(money):
        if isinstance(money, float) and money >= 0.0:
            return True
        return False