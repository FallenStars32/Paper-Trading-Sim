import Function_Exucations

def request_credentials():
    command1 = input("--sign in \n"
                     "--sign up\n")
    accounts = account(command1)

    return accounts



def account(command1):
    if command1 == "--sign in":
        # Code for the database you connect to
        username = "username1"
        return username
    elif command1 == "--sign up":
        username = "username1"
        return username
    else:
        print("Error: Could not understand command")
        request_credentials()

def actions(account):
    command2 = input("--buy STOCK ticker AMOUNT\n"
                     "--sell STOCK ticker AMOUNT\n"
                     "--buy OPTION option_ticker\n"
                     "--sell OPTION option_ticker\n"
                     "--current portfolio value\n")
    result = interpret(command2, account)
    if result == 1:
        print("Error: Could not understand input")
        request_credentials()
    elif result == 2:
        print("Error: The NYSE is closed")
        request_credentials()
    elif result == 3:
        print("Error: The ticker does not exist according to our records")
        request_credentials()
    elif result == 4000:
        print("Error: You do not have enough money for this order")
    elif result == 5:
        print("Error: An unknown error happened")
    elif result == 6:
        print("Error: Could not proccese cash")
    elif result[0] == 4:
        print(f"Succesfully {result[1]} {result[2]} shares of {result[3]} @ {result[6]}")
        print(f"You have ${result[4]} left. The order costed {result[5]}")


def interpret(command2, account):
    command_parts = command2.split()
    action = command_parts[0]
    ticker = command_parts[2]

    if action == "--buy" and command_parts[1] == "STOCK":
        amount = int(command_parts[3])
        result = Function_Exucations.buy_stock(ticker, amount, account)
        if result == 1000:
            pass
        if result == 1001:
            return 3
        if result == 3000:
            return 6
        else:
            return result

    elif action == "--sell" and command_parts[1] == "STOCK":
        amount = int(command_parts[3])
        result = Function_Exucations.sell_stock_check(ticker, amount, account)
        if result == 1000:
            return 2
        if result == 1001:
            return 3
        else:
            return 4, action, amount, ticker


    elif action == "--buy" and command_parts[1] == "OPTION":
        print(f"Buying option {ticker}")

    elif action == "--sell" and command_parts[1] == "OPTION":
        print(f"Selling option {ticker}")
    elif command2 == "--current portfolio value":
        print(account_value(account))
        actions(account)
    else:
        return 1

def account_value(account):
    return Function_Exucations.calculate_account_value(f"{account}_stocks.csv")


actions(request_credentials())


