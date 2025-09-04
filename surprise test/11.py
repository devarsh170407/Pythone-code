numbers=[12,23]
product=1
for n in numbers:
    last_digit=n%10   
    product=product*last_digit   
print(product)