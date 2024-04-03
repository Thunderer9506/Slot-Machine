MAX_LINES = 3

def deposit():
    while True:
        amount = input("What would you like to deposit? ₹")
        if amount.isdigit():
            if int(amount) > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():
            if 1<= int(lines) <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number")
    return lines

def main():
    balance = deposit()
    lines = get_number_of_lines()

main()