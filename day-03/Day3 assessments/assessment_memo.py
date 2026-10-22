print("Input one of the following tickets category : " ,"\n" ,"# Standard" ,"\n","# VIP","\n","# WIP")

ticket_category = input(" Please enter ticket category :") 
number_of_tickets = float(input("Please enter number of tickets : "))

if ticket_category == "Standard":
    price = 150
else:
     if ticket_category == "VIP":
         price = 350
     else:
        if ticket_category == "VVIP":
            price = 500
    

subtotal = price * number_of_tickets
tax_amount = subtotal * 0.07
totalcost = subtotal + tax_amount

print("Number of tickets are " , number_of_tickets)
print("Tax Amount is equal to  " , f"{tax_amount:.2f}" )
print("Total Cost is equal R ",f"{totalcost:.2f}")

   
    