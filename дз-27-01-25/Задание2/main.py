from CreditCard import CreditCard
from PaymentForm import PaymentForm
from datetime import date

card = CreditCard("1234567891234567", "Виктор Морозов", date(2026,12,25), "123", 250.0)
payment_form = PaymentForm(card)
#Получение данных карты
print(f"Карта:{card.getCardNumber()}")
print(f"Владелец:{card.getCardHolder()}")
print(f"Срок действия:{card.getExpiryDate()}")
print(f"CVC:{card.getCvv()}")
#Обработка платежа 
amount=100.00
result=payment_form.pay(amount)
print(result)
#Попытка чрезмерного списания
try:
    card.charge(1500.00)
#Это вызовет исключение
except Exception as e:
    print(f"Ошибка при попытке чрезмерного списания: {e}")

#Успешный платеж
result=payment_form.pay(50.00)
print(result)