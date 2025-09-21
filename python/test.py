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

dict_orders = {
    "order 1": {
        "amount": 18,
        "status": "доставлен"
    },
    "order 2": {
        "amount": 20,
        "status": "доставлен"
    },
    "order 3": {
        "amount": 15,
        "status": "отменен"
    },
    "order 4": {
        "amount": 10,
        "status": "доставлен"
    },
    "order 5": {
        "amount": 25,
        "status": "отменен"
    },
    "order 6": {
        "amount": 30,
        "status": "в пути"
    }
}
"""
переделать решение с использованием словаря
"""

delivered_amount = 0
order_names = []

for order in orders:
    order_names.append(order[0])

    if order[2] == 'доставлен':
        delivered_amount += 1
        
print(delivered_amount)
print(order_names)

#print(dict_orders["order 1"])

print(sum(1 if order["status"] == "доставлен" else 0 for order in dict_orders.values()))
print(list(dict_orders.keys()))

delivered_amount = 0
for order in dict_orders.values():
    if order["status"] == "доставлен":
        delivered_amount += 1

print(delivered_amount)
