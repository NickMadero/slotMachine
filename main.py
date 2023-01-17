# this function will be responible for collecting user input that gets the deposit from the user
#this is like saying a constant variable in all caps 
MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1
def deposit():
    while True:
        amount  = input("what would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("amount must be greater than 0")
        else:
            print("please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines  = input("enter the number of lines you want to bet on (1-" + str(MAX_LINE)+" )?")
        if lines.isdigit():
            lines = int(lines)
            if  1 <= lines <= MAX_LINE:
                break
            else:
                print("enter a valild number ")
        else:
            print("please enter a number")
    return lines

def get_bet():
    while True:
        amount  = input("what would you like to bet? on each line $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break
            else:
                print(f"amount must be between{MIN_BET} - {MAX_BET}")
        else:
            print("please enter a number")
    return amount
def main() :
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet>= balance:
            print(f"you do not have enough money to bet that amount your current balance is ${balance}")
        else :
            break
    print(f"your are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")




main()