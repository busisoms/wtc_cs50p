"""
Program that prompts the user to insert a coin, 
one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents,
output how many cents in change the user is owed.
"""

def main():
    amount_owed = 50

    while True:
        print(f"Amount Due: {amount_owed}")
        coin = int(input("Insert Coin: "))

        if coin == 5 or coin == 10 or coin == 25:
            amount_owed -= coin
            
            if amount_owed <= 0:
                print(f"Change Owed: {(amount_owed) * -1}")
                break
        else:
            continue

main()