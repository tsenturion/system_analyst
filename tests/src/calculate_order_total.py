def calculate_order_total(items, tax_rate=0.0, discount_code=None):
    """
    Рассчитывает итоговую сумму заказа.

    items: список словарей, каждый из которых содержит:
        - name: название товара
        - price: цена за единицу (float)
        - quantity: количество (int)

    tax_rate: налоговая ставка (например, 0.1 для 10%)

    discount_code: может быть строкой:
        - "SALE10" → скидка 10%
        - "SALE20" → скидка 20%
        - None → без скидки
    """
    if not items:
        raise ValueError("Список товаров не может быть пустым")

    subtotal = 0
    for item in items:
        if item['price'] < 0 or item['quantity'] < 0:
            raise ValueError("Цена и количество не могут быть отрицательными")
        subtotal += item['price'] * item['quantity']

    if discount_code == "SALE10":
        subtotal *= 0.90
    elif discount_code == "SALE20":
        subtotal *= 0.80
    elif discount_code is not None:
        raise ValueError("Недопустимый код скидки")

    total = subtotal * (1 + tax_rate)
    return round(total, 2)
