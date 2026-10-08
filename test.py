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
    print("============== RECEIPT ===============")
    while(i<len(products)):
        product = products[i]
        quantity = quantities[i]
        price = prices[i]
        itemTotal = quantity * price
        subTotal += itemTotal

        print(f"{product}: {quantity}*{price}")
        i += 1
    tax = subTotal * 0.13
    total = subTotal + tax
    print("--------------------------------------")
    print(f"Subtotal:{subTotal}")
    print(f"Tax (13%):{tax}")
    print(f"Total:{total}")
    print("======================================")
products = ["Trail Backpack", "Water Bottle", "Headlamp"]
quantities = [3, 2, 1]
prices = [89.99, 12.50, 34.00]
    
print_receipt(products, quantities, prices)

# def print_receipt(products, quantities, prices):
#     i = 0
#     subtotal = 0

#     print("============== RECEIPT ===============")

#     while i < len(products):
#         product = products[i]
#         quantity = quantities[i]
#         price = prices[i]

#         item_total = quantity * price
#         subtotal += item_total

#         print(f"{product:<16} {quantity} x {price:6.2f} = {item_total:7.2f}")

#         i += 1

#     tax = subtotal * 0.13
#     total = subtotal + tax

#     print("--------------------------------------")
#     print(f"Subtotal:                     {subtotal:7.2f}")
#     print(f"Tax (13%):                    {tax:7.2f}")
#     print(f"Total:                        {total:7.2f}")
#     print("======================================")


# products = ["Trail Backpack", "Water Bottle", "Headlamp"]
# quantities = [3, 2, 1]
# prices = [89.99, 12.50, 34.00]

# print_receipt(products, quantities, prices)


