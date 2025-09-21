"""
создать переменные заказов в списке
переменная количества доставленных, названий

функцией длины 
в цикле, если доставлен в статусах, увеличить переменную количества доставленных
в цикле в переменную название товара
"""

orders = [
    ['order 1', 18, 'доставлен'],
    ['order 2', 20, 'доставлен'],
    ['order 3', 15, 'отменен'],
    ['order 4', 10, 'доставлен'],
    ['order 5', 25, 'отменен'],
    ['order 6', 30, 'в пути'],
]

delivered_amount = 0
order_names = []

for order in orders:
    order_names.append(order[0])

    if order[2] == 'доставлен':
        delivered_amount += 1
        
print(delivered_amount)
print(order_names)