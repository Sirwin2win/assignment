def parse_order(raw_order):
    stripedOrder = raw_order.strip()
    splittedOrder = [i for i in stripedOrder.split('|')]
    order_id = splittedOrder[0]
    product = splittedOrder[1]
    quantity = int(splittedOrder[2])
    unit_price = float(splittedOrder[3])

    return order_id, product, quantity, unit_price
raw_order = "  ORD-2041 | Trail Backpack | 3 | 89.99  "
order_id, product, quantity, unit_price = parse_order(raw_order)
print(order_id, product, quantity, unit_price)

def print_receipt(products, quantities, prices):
    i = 0
    subTotal = 0
    while(i<products.length):
        product = products[i]
        quantity = quantity[i]
        price = price[i]
        itemTotal = quantity * price
        subtotal += itemTotal

        print(f"{product}: {quantity}*{price}")
        i++
    tax = subtotal * 0.13
    total = subtotal + tax


