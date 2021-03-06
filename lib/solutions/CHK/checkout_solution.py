
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    price = 0

    products = {}
    product_count = {}

    group = ["S","T","X","Y","Z"]

    used_pairs = []

    pairs_found = False
    found = False

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
    products["K"] = 70
    products["L"] = 90
    products["M"] = 15
    products["N"] = 40
    products["O"] = 10
    products["P"] = 50
    products["Q"] = 30
    products["R"] = 50
    products["S"] = 20
    products["T"] = 20
    products["U"] = 40
    products["V"] = 50
    products["W"] = 20
    products["X"] = 17
    products["Y"] = 20
    products["Z"] = 21

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


    while pairs_found is False:

        t = 3
        n = 0

        while n < 3:

            if found is True:

                n = 0

                found = False

            for j in range(2,5-n):

                print("N = ", n)

                if product_count[group[n]][0] > 0 and product_count[group[n+1]][0] > 0 and product_count[group[n+j]][0] > 0:

                    product_count[group[n]] = (product_count[group[n]][0] - 1, (product_count[group[n]][0] - 1) * products[group[n]])
                    product_count[group[n+1]] = (product_count[group[n+1]][0] - 1, (product_count[group[n+1]][0] - 1) * products[group[n+1]])
                    product_count[group[n+j]] = (product_count[group[n+j]][0] - 1, (product_count[group[n+j]][0] - 1) * products[group[n+j]])

                    price = price + 45

                    used_pairs.append((group[n],group[n+1], group[n+j]))

                    print("Pair found")

                    found = True

            n = n + 1



        pairs_found = True

    pairs_found = False

    while pairs_found is False:

        n = 0

        while n < 5:

            if found is True:

                n = 0

                found = False

            for j in range(0,5):

                if n == j:
                    pass

                elif product_count[group[n]][0] >= 2 and product_count[group[j]][0] > 0:

                    product_count[group[n]] = (
                    product_count[group[n]][0] - 2, (product_count[group[n]][0] - 2) * products[group[n]])
                    product_count[group[j]] = (
                    product_count[group[j]][0] - 1, (product_count[group[j]][0] - 1) * products[group[j]])

                    price = price + 45

                    found = True

            n = n + 1

        pairs_found = True


    for n in range(0,5):

        if product_count[group[n]][0] >= 3:
            product_count[group[n]] = (product_count[group[n]][0] - 3, (product_count[group[n]][0] - 3) * products[group[n]])

            price = price + 45



    for prods in product_count:

        if prods == "E":

            total = product_count["E"][0]
            total_b = product_count["B"][0]

            if total // 2 > 0:

                total_b = total_b - (total // 2)

                print(total_b)

                if (total_b < 0):
                    total_b = 0

                product_count["B"] = (total_b, product_count["B"][1])


        if prods == "F":

            total = product_count["F"][0]

            if total // 3 > 0:

                product_count["F"] = ((product_count["F"][0] - (total//3)), (product_count["F"][0] - (total//3)) * products["F"])


        if prods == "N":

            total = product_count["N"][0]
            total_b = product_count["M"][0]

            if total // 3 > 0:

                total_b = total_b - (total // 3)

                print(total_b)

                if (total_b < 0):
                    total_b = 0

                product_count["M"] = (total_b, total_b * products["M"])


        if prods == "R":

            total = product_count["R"][0]
            total_b = product_count["Q"][0]

            if total // 3 > 0:

                total_b = total_b - (total // 3)

                print(total_b)

                if (total_b < 0):
                    total_b = 0

                product_count["Q"] = (total_b, total_b * products["Q"])


        if prods == "U":

            total = product_count["U"][0]

            if total // 4 > 0:

                product_count["U"] = ((product_count["U"][0] - (total//4)), (product_count["U"][0] - (total//4)) * products["U"])



    for prods in product_count:

        #print(products)

        if prods == "A":

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

        if prods == "B":

            new_price = 0

            total = product_count["B"][0]

            print("B total: ", total)

            if total // 2 > 0:

                #print(total)
                new_price = new_price + 45 * (total // 2)
                total = total - (2*(total//2))
                #print(total)

            if total > 0:

                new_price = new_price + (total * products["B"])


            product_count["B"] = (product_count["B"][0], new_price)

        if prods == "H":

            new_price = 0

            total = product_count["H"][0]

            if total // 10 > 0:

                print(total)
                new_price = new_price + 80 * (total // 10)
                total = total - (10*(total//10))
                print(total)

            if total // 5 > 0:

                new_price = new_price + 45 * (total//5)
                total = total - (5*(total//5))

            if total > 0:

                new_price = new_price + (total * products["H"])


            product_count["H"] = (product_count["H"][0], new_price)

        if prods == "K":

            new_price = 0

            total = product_count["K"][0]

            print("B total: ", total)

            if total // 2 > 0:
                # print(total)
                new_price = new_price + 120 * (total // 2)
                total = total - (2 * (total // 2))
                # print(total)

            if total > 0:
                new_price = new_price + (total * products["K"])

            product_count["K"] = (product_count["K"][0], new_price)

        if prods == "P":

            new_price = 0

            total = product_count["P"][0]

            print("B total: ", total)

            if total // 5 > 0:
                # print(total)
                new_price = new_price + 200 * (total // 5)
                total = total - (5 * (total // 5))
                # print(total)

            if total > 0:
                new_price = new_price + (total * products["P"])

            product_count["P"] = (product_count["P"][0], new_price)

        if prods == "Q":

            new_price = 0

            total = product_count["Q"][0]

            print("B total: ", total)

            if total // 3 > 0:
                # print(total)
                new_price = new_price + 80 * (total // 3)
                total = total - (3 * (total // 3))
                # print(total)

            if total > 0:
                new_price = new_price + (total * products["Q"])

            product_count["Q"] = (product_count["Q"][0], new_price)

        if prods == "V":

            new_price = 0

            total = product_count["V"][0]

            if total // 3 > 0:

                new_price = new_price + 130 * (total//3)
                total = total - (3*(total//3))


            if total // 2 > 0:

                print(total)
                new_price = new_price + 90 * (total // 2)
                total = total - (2*(total//2))
                print(total)

            if total > 0:

                new_price = new_price + (total * products["V"])


            product_count["V"] = (product_count["V"][0], new_price)

    for prods in product_count:

        price = price + product_count[prods][1]

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




print(checkout("ZZZS"))
