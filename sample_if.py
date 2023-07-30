def new_price(price_before, sale_):
    new_price_ = price_before - price_before * sale_ / 100
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
