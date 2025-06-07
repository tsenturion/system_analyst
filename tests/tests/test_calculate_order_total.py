import pytest
from src.calculate_order_total import calculate_order_total

def test_basic_order():
    items = [
        {'name': 'Book', 'price': 10.0, 'quantity': 2},
        {'name': 'Pen', 'price': 5.0, 'quantity': 1}
    ]
    result = calculate_order_total(items)
    assert result == 25.0

def test_order_with_tax():
    items = [
        {'name': 'Bag', 'price': 20.0, 'quantity': 1},
    ]
    result = calculate_order_total(items, tax_rate=0.1)
    assert result == 22.0

def test_order_with_sale10_discount():
    items = [
        {'name': 'Shirt', 'price': 30.0, 'quantity': 1},
    ]
    result = calculate_order_total(items, discount_code='SALE10')
    assert result == 27.0

def test_order_with_sale20_discount():
    items = [
        {'name': 'Panst', 'price': 50.0, 'quantity': 1},
    ]
    result = calculate_order_total(items, discount_code='SALE20')
    assert result == 40.0

def test_discount_and_tax():
    items = [
        {'name': 'Shoes', 'price': 100.0, 'quantity': 1},
    ]
    result = calculate_order_total(items, discount_code='SALE10', tax_rate=0.1)
    assert result == 99.0

def test_invalid_discount_code():
    items = [
        {'name': 'Item', 'price': 10.0, 'quantity': 1},
    ]
    with pytest.raises(ValueError, match='Недопустимый код скидки'):
        calculate_order_total(items, discount_code='INVALID')

def test_negative_price():
    items = [
        {'name': 'Faulty', 'price': -5.0, 'quantity': 1},
    ]
    with pytest.raises(ValueError, match='Цена и количество не могут быть отрицательными'):
        calculate_order_total(items)

def test_negative_quantity():
    items = [
        {'name': 'Faulty', 'price': 5.0, 'quantity': -1},
    ]
    with pytest.raises(ValueError, match='Цена и количество не могут быть отрицательными'):
        calculate_order_total(items)

def test_empty_items_list():
    with pytest.raises(ValueError, match='Список товаров не может быть пустым'):
        calculate_order_total([])

def test_rounding():
    items = [
        {'name': 'Item', 'price': 19.999, 'quantity': 1},
    ]
    result = calculate_order_total(items)
    assert result == 20.0
    