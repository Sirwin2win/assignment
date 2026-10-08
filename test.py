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


def describe(scores, display=True):
    count = len(scores)

    if count == 0:
        raise ValueError("scores cannot be empty")

    mean = sum(scores) / count

    # Sample standard deviation
    if count > 1:
        variance = sum((x - mean) ** 2 for x in scores) / (count - 1)
        std = variance ** 0.5
    else:
        std = 0.0

    sorted_scores = sorted(scores)

    # Calculate percentiles using linear interpolation
    def percentile(data, p):
        position = (len(data) - 1) * p
        lower = int(position)
        upper = min(lower + 1, len(data) - 1)
        fraction = position - lower

        return data[lower] + fraction * (data[upper] - data[lower])

    results = {
        "count": count,
        "mean": mean,
        "std": std,
        "min": sorted_scores[0],
        "25%": percentile(sorted_scores, 0.25),
        "50%": percentile(sorted_scores, 0.50),
        "75%": percentile(sorted_scores, 0.75),
        "max": sorted_scores[-1]
    }

    if display:
        print("Summary Statistics")
        print("------------------")
        print(f"count    {count}")
        print(f"mean     {mean:.2f}")
        print(f"std      {std:.2f}")
        print(f"min      {results['min']:.2f}")
        print(f"25%      {results['25%']:.2f}")
        print(f"50%      {results['50%']:.2f}")
        print(f"75%      {results['75%']:.2f}")
        print(f"max      {results['max']:.2f}")

    return results


scores = [12, 15, 11, 18, 20, 14, 16, 13]

results = describe(scores)
# Prints the summary and returns the dictionary

results = describe(scores, display=False)
# Returns the dictionary without printing

def word_frequency(text):
    # Convert all text to lowercase
    text = text.lower()

    # Remove punctuation
    for punctuation in ".,!?;:'\"":
        text = text.replace(punctuation, "")

    # Split the text into individual words
    words = text.split()

    # Count each word
    frequencies = {}

    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    return frequencies


text = "The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs away!"

frequencies = word_frequency(text)

print(frequencies)


