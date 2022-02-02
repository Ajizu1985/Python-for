
price = float(input("Enter price:"))

for item in range (1, 11):
    convert = item/10
    retail_price = convert * price
    print(f"{convert} kg is {retail_price} UZS")