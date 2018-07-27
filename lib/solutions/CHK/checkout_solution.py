
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    a_count = 0
    e_count = 0
    f_count = 0
    total_a = 0
    total_b = 0
    b_count = 0
    price = 0

    products = {}

    products["A"] = 50
    products["B"] = 30
    products["C"] = 20
    products["D"] = 15
    products["E"] = 40
    products["F"] = 10

    for product in skus:

        if product not in products:

            return -1

        if product == "A":

            a_count = a_count + 1
            total_a = total_a + 1

        if product == "B":

            b_count = b_count + 1
            total_b = total_b + 1

        if product == "E":

            e_count = e_count + 1

        if product == "F":

            f_count = f_count + 1


        price = price + products[product]

        if a_count == 3:
            price = price - 20
            a_count = 0

        if total_a == 5:

            price = price - 30
            total_a = 0
            a_count = 0

        if b_count == 2:
            price = price - 15
            b_count = 0

        if e_count >= 2 and total_b > 0:

            if total_b % 2 == 0:

                price = price - 15
                total_b = total_b - 1
                b_count = b_count - 1

            else:

                price = price - 30
                total_b = total_b - 1
                b_count = b_count - 1

            e_count = e_count - 2

        if f_count == 3:

            price = price - 10
            f_count = 0



    return price


print(checkout("FFFFFFFF"))