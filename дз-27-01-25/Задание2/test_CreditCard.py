from CreditCard import CreditCard
import pytest

from unittest.mock import MagicMock
from datetime import date


CardNumber ="1234567891234567"
CardHolder = "Виктор Морозов"
ExpiryDate = date(2026,12,25)
Cvv =  "123"
Money = 250.0


@pytest.fixture
def credit_card():
    '''Возвращает заполненную кредитную карту для тестирования'''
    credit_card = CreditCard(CardNumber,CardHolder, ExpiryDate, Cvv, Money)
    yield credit_card

@pytest.fixture
def mock_credit_card():
    '''Возвращает мок-обьект для класса CreditCard'''
    card = MagicMock(spec=CreditCard)
    card.charge.return_value = True
    yield card

#Тесты для CreditCard
def test_getCardNumber_passed(credit_card):
    '''
        Тест проверяет метод getCardNumber на правильное возвращение значения\n
        Метод должен возвращать номер карты
    '''
    assert credit_card.getCardNumber() == CardNumber

def test_getCardHolder_passed(credit_card):
    '''
        Тест проверяет метод getCardHolder на правильное возвращение значения\n
        Метод должен возвращать владельца карты
    '''
    assert credit_card.getCardHolder() == CardHolder


def test_getExpiryDate_passed(credit_card):
    '''
        Тест проверяет метод getExpiryDate на правильное возвращение значения\n
        Метод должен возвращать срок годности
    '''
    assert credit_card.getExpiryDate() == ExpiryDate

def test_getCvv_passed(credit_card):
    '''
        Тест проверяет метод getCvv на правильное возвращение значения\n
        Метод должен возвращать cvv-код карты
    '''
    assert credit_card.getCvv() == Cvv


def test_charge_passed(mock_credit_card):
    '''
        Тест проверяет корректность вызова метода charge\n
        Используется мок-обьект. Его функция charge должна возвращать True.
        После идет проверка вывода метода из мок-обьекта
    '''
    assert mock_credit_card.charge() == True
    mock_credit_card.charge.assert_called_once()

@pytest.mark.parametrize('amount', [
    ("money"),
    (False)
])
def test_charge_invalid_amount_type(amount, credit_card):
    '''
        Тест проверяет защиту метода charge от ввода значений недопустимых типов\n
        Метод должен выбрасывать исключение
    '''
    with pytest.raises(Exception):
        credit_card.charge(amount)


def test_charge_not_enough_money(credit_card):
     '''
        Тест проверяет защиту метода charge от ввода значений превыщаюших баланс\n
        Метод должен выбрасывать исключение
    '''
     with pytest.raises(Exception):
        credit_card.charge(Money+100.0)

def test_charge_negative_amount(credit_card):
     '''
        Тест проверяет защиту метода charge от ввода значений меньше нуля\n
        Метод должен выбрасывать исключение
    '''
     with pytest.raises(Exception):
        credit_card.charge(-10.0)

@pytest.mark.parametrize('data', [
    ("*&^"),
    (False)
])
def test_credit_card_input(data):
    '''
        Тест проверяет защиту консируктора CreditCard от ввода значений недопустимых типов\n
        Конструктор должен выбрасывать исключение
    '''
    with pytest.raises(Exception):
        CreditCard(cardNumber = data)
    with pytest.raises(Exception):
        CreditCard(cardHolder = data)
    with pytest.raises(Exception):
        CreditCard(expiryDate = data)
    with pytest.raises(Exception):
        CreditCard(cvv = data)
    with pytest.raises(Exception):
        CreditCard(money = data)