# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
# If it is a loss, calculate the loss and print it
# If it is a profit, calculate the profit and print it
# If the cost price and selling price are equal, print "No profit, no loss"
# If the cost price is greater than the selling price, print "Loss"
# If the cost price is less than the selling price, print "Profit"
# If the cost price is equal to the selling price, print "No profit, no loss"

def calculate_profit_or_loss(cp, sp):
    if cp > sp:
        loss = cp - sp
        loss_percentage = (loss / cp) * 100
        print("Loss: ", loss, "Loss percentage: ", loss_percentage, "%")
    elif cp < sp:
        profit = sp - cp
        profit_percentage = (profit / cp ) * 100
        print("Profit: ", profit, "Profit percentage: ", profit_percentage)

    else:
        print("No profit, no loss")


# Taking input for cost price and selling price
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

calculate_profit_or_loss(cost_price, selling_price)


