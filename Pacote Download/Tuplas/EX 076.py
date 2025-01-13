products = ('Milk', 3.00, 'Bread', 1.00, 'Lettuce', 3.50, 'Garlic', 2.23, 'Tomato', 4.50, 'Creatine', 100.1)

print("WELCOME TO MY MINI-MARKET\nChoose what you wanna buy:")
for i in range(0, len(products), 2):
    product = products[i]
    price = products[i + 1]
    print('Product: {}............ Price: {:.2}'.format(product, price))
print("\nI am backing to my house, my house is vs code and the programming world, I have a lot of difficult with python, but all the these difficults will pass away")
