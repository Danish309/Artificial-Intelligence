# -----------------Question----------------------------------------------------------------------

# A man walks into a store to buy some items. His total bill is rupees X. He pays the cashier
# rupees Y. The cashier now has to return him change (Y-X). Write a code using greedy algorithm
# to find out how many denominations of each note will the cashier return. You must take user
# input for values of X and Y
# Use the following numbers for denomination: 100 50 20 10 5 2 1

# -------------------------Code--------------------------------------------------------------------

denominations = [100, 50, 20, 10, 5, 2, 1]
x = int(input("Total Bill (x): "))
j = 0
i = 0
while j == 0:
    y = int(input("Amount Paid (y): "))

    if y >= x:
        change = y - x
        print("Change is: ", change)
        print("Denominations of the change is: ")
        while i < len(denominations):
            if denominations[i] <= change:
                print(denominations[i])
                change -= denominations[i]


            else:
                i += 1
        j = 1
