
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    price = 0

    products = {}
    product_count = {}

    products["A"] = 50
    products["B"] = 30
    products["C"] = 20
    products["D"] = 15
    products["E"] = 40
    products["F"] = 10
    products["G"] = 20
    products["H"] = 10
    products["I"] = 35
    products["J"] = 60
    products["K"] = 80
    products["L"] = 90
    products["M"] = 15
    products["N"] = 40
    products["O"] = 10
    products["P"] = 50
    products["Q"] = 30
    products["R"] = 50
    products["S"] = 30
    products["T"] = 20
    products["U"] = 40
    products["V"] = 50
    products["W"] = 20
    products["X"] = 90
    products["Y"] = 10
    products["Z"] = 50

    product_count["A"] = (0,0)
    product_count["B"] = (0,0)
    product_count["C"] = (0,0)
    product_count["D"] = (0,0)
    product_count["E"] = (0,0)
    product_count["F"] = (0,0)
    product_count["G"] = (0,0)
    product_count["H"] = (0,0)
    product_count["I"] = (0,0)
    product_count["J"] = (0,0)
    product_count["K"] = (0,0)
    product_count["L"] = (0,0)
    product_count["M"] = (0,0)
    product_count["N"] = (0,0)
    product_count["O"] = (0,0)
    product_count["P"] = (0,0)
    product_count["Q"] = (0,0)
    product_count["R"] = (0,0)
    product_count["S"] = (0,0)
    product_count["T"] = (0,0)
    product_count["U"] = (0,0)
    product_count["V"] = (0,0)
    product_count["W"] = (0,0)
    product_count["X"] = (0,0)
    product_count["Y"] = (0,0)
    product_count["Z"] = (0,0)

    for product in skus:

        if product not in products:

            return -1


        product_count[product] = (product_count[product][0] + 1, product_count[product][1] + products[product])


    for products in product_count:

        #print(products)

        if products == "A":

            new_price = 0

            total = product_count["A"][0]

            if total // 5 > 0:

                new_price = new_price + 200 * (total//5)
                total = total - (5*(total//5))


            if total // 3 > 0:

                print(total)
                new_price = new_price + 130 * (total // 3)
                total = total - (3*(total//3))
                print(total)

            if total > 0:

                new_price = new_price + (total * products["A"])


            product_count["A"] = (product_count["A"][0], new_price)

            price = price + product_count["A"][1]

        if products == "B":

            new_price = 0

            total = product_count["B"][0]

            if total // 2 > 0:

                print(total)
                new_price = new_price + 45 * (total // 2)
                total = total - (2*(total//2))
                print(total)

            if total > 0:

                new_price = new_price + (total * products["B"])


            product_count["B"] = (product_count["B"][0], new_price)

            price = price + product_count["B"][1]


    return price


 # if product == "A":
        #
        #     a_count = a_count + 1
        #     total_a = total_a + 1
        #
        # if product == "B":
        #
        #     b_count = b_count + 1
        #     total_b = total_b + 1
        #
        # if product == "E":
        #
        #     e_count = e_count + 1
        #
        # if product == "F":
        #
        #     f_count = f_count + 1
        #
        #
        # price = price + products[product]
        #
        # if a_count == 3:
        #     price = price - 20
        #     a_count = 0
        #
        # if total_a == 5:
        #
        #     price = price - 30
        #     total_a = 0
        #     a_count = 0
        #
        # if b_count == 2:
        #     price = price - 15
        #     b_count = 0
        #
        # if e_count >= 2 and total_b > 0:
        #
        #     if total_b % 2 == 0:
        #
        #         price = price - 15
        #         total_b = total_b - 1
        #         b_count = b_count - 1
        #
        #     else:
        #
        #         price = price - 30
        #         total_b = total_b - 1
        #         b_count = b_count - 1
        #
        #     e_count = e_count - 2
        #
        # if f_count == 3:
        #
        #     price = price - 10
        #     f_count = 0




print(checkout("A"))
