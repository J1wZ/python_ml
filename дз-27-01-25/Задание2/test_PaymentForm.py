from CreditCard import CreditCard
from PaymentForm import PaymentForm
import pytest

from unittest.mock import MagicMock

@pytest.fixture
def mock_credit_card():
    '''Возвращает мок-обьект для класса CreditCard'''
    card = MagicMock(spec=CreditCard)
    card.charge.return_value = True
    yield card

#Тесты для PaymentForm
def test_pay_with_mock_credit_card_passed(mock_credit_card):
    '''
        Тест проверяет метод pay на вызов метода charge\n
        Вместо класса CreditCard используется мок-обьект для этого класса.
        Метод должен возвращать True.
        Потом идет проверка на вызов метода мок-обьекта
    ''' 
    payment_form = PaymentForm(mock_credit_card)
    result=payment_form.pay(100)
    assert result == True
    mock_credit_card.charge.assert_called_once_with(100)


@pytest.mark.parametrize('amount', [
    ("-759"),
    (True)
])
def test_pay_invalid_amount_type(amount,mock_credit_card):
    '''
        Тест проверяет защиту метода pay от ввода значений недопустимых типов\n
        Вместо класса CreditCard используется мок-обьект для этого класса.
        Метод должен выбрасывать исключение.
        Потом идет проверка на вызов метода мок-обьекта
    ''' 
    mock_credit_card.charge.side_effect = Exception("Mock Error!")
    payment_form = PaymentForm(mock_credit_card)
    with pytest.raises(Exception):
        payment_form.pay(amount)
    mock_credit_card.charge.assert_called_once_with(amount)

def test_pay_not_enough_money(mock_credit_card):
    '''
        Тест проверяет защиту метода pay от ввода значений превыщаюших баланс\n
        Вместо класса CreditCard используется мок-обьект для этого класса.
        Метод должен выбрасывать исключение.
        Потом идет проверка на вызов метода мок-обьекта
    ''' 
    mock_credit_card.charge.side_effect = Exception("Mock Error!")
    payment_form = PaymentForm(mock_credit_card)
    with pytest.raises(Exception):
        payment_form.pay(100)
    mock_credit_card.charge.assert_called_once_with(100)

def test_pay_negative_amount(mock_credit_card):
    '''
        Тест проверяет защиту метода pay от ввода значений меньше нуля\n
        Вместо класса CreditCard используется мок-обьект для этого класса.
        Метод должен выбрасывать исключение.
        Потом идет проверка на вызов метода мок-обьекта
    '''  
    mock_credit_card.charge.side_effect = Exception("Mock Error!")
    payment_form = PaymentForm(mock_credit_card)
    with pytest.raises(Exception):
        payment_form.pay(-100)
    mock_credit_card.charge.assert_called_once_with(-100)