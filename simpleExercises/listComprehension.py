exclude = [chr(i) for i in range(70, 80) if i % 2 != 0]
result = [chr(i) for i in range(65, 91) if chr(i) not in exclude]
print(result)

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

tshirts = [(i, j) for i in colors for j in sizes]
print(tshirts)

sold_out = [('Black', 'm'), ('White', 's')]
tshirts_available = [(i, j) for i in colors for j in sizes if (i, j) not in sold_out]
print(tshirts_available)

