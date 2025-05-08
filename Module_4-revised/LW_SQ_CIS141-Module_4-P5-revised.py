#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. Ask the user for the order total and print the total cost, including shipping.

totalcheckout = int(input("Total checkout: "))
if int(totalcheckout) >= 50:
    print(f"Shipping is free. \nCheckout: {totalcheckout}")
else:
    print(f"Shipping is $5. \nCheckout: {totalcheckout + 5}")