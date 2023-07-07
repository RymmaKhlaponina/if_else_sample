""" Write a program that outputs to the console the new price of the product, including the discount,
IF there is a discount
1) Create a main function
2) Create in main a variable, in which the console will write the cost of the goods
3) Print the message "Is the product on sale (0/1)?" and write the value entered from the console into the variable
4) If the user enters 1 from the console - enter the discount value (without %)
5) Create a function that calculates the new value of the goods with a discount and output the result on the console."""


def new_price(price_before, sale_):
    new_price_ = price_before - price_before*sale_/100
    return new_price_


def main():
    price = float(input("Write the price of the product: "))
    sale_or = int(input("Is this product eligible for a discount?\n Write 0 if No\n Write 1 if Yes\n: "))
    if sale_or == 1:
        sale = int(input("Write the discount that applies to the product (without the % sign): "))
        print("Prise with a sale: ", + new_price(price, sale))
    else:
        print("This product is not included in the sale. Current price:", price)


main()

