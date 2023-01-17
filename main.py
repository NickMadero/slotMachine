import random
#this is like saying a constant variable in all caps 

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3 

symbol_count = {
    "A":  2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A":  5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winnings_lines = []

    for line in range(lines): #every line in the lines 
        symbol = columns[0][line] # symbol is whaever symbol in hte 
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_count:
                break
        else :
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1 )
    return winnings, winnings_lines


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i , column in enumerate(columns):
            if i != len(columns) -1 :
             print(column[row],"|", end=" | ")
            else:
                print(column[row],end="")
        print()

# this function will be responible for collecting user input that gets the deposit from the user
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



# get number of lines will ask the user to enter how many lines they want to bet on 
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


# get bet will ask the user how much they want to bet on each line
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

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet>= balance:
            print(f"you do not have enough money to bet that amount your current balance is ${balance}")
        else :
            break
    print(f"your are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")


    slots = get_slot_machine_spin(ROWS,COLS, symbol_count)
    print_slot_machine(slots)
    winnings , winning_line = check_winnings(slots,lines,bet,symbol_value)
    print(f"you won ${winnings}")
    print(f"you won on lines:", *winning_line)
    return winnings - total_bet
# this is main where we can call our functions 
def main() :
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        answer = input("press enter to spin( q to quit ) ")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"you left with ${balance}")
# calls main 
main()