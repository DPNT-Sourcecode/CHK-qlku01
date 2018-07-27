
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    a_count = 0
    b_count = 0
    price = 0

    products = {}

    products["A"] = 50
    products["B"] = 30
    products["C"] = 20
    products["D"] = 15

    for product in skus:

        if product not in products:

            return -1

        if product == "A":

            a_count = a_count + 1

        if product == "B":

            b_count = b_count + 1

        
        price = price + products[product]

        if a_count == 3:
            price = price - 20
            a_count = 0

        if b_count == 2:
            price = price - 15
            b_count = 0



    return price