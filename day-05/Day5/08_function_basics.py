def calc_total(item):
    base_price = 25.5
    vat = 0.15
    total = ( base_price * len(item)) + 1.15
    return total

myfood = input("get items :")  
order_total = calc_total(myfood)
print(f'Your order costs: R {order_total:.2f}')
#f'Your order costs: R {round(order_total,2)}