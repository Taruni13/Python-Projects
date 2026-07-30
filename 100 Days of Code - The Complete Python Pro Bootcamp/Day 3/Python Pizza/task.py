print("Welcome to Python Pizza Deliveries!")

# Get user input and normalize case
size = input("What size pizza do you want? S, M or L: ").strip().upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").strip().upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").strip().upper()

bill = 0

# Validate size and calculate base price
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid size selected. Please choose S, M, or L.")
    exit()

# Add pepperoni cost
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
elif pepperoni != "N":
    print("Invalid input for pepperoni. Please choose Y or N.")
    exit()

# Add extra cheese cost
if extra_cheese == "Y":
    bill += 1
elif extra_cheese != "N":
    print("Invalid input for extra cheese. Please choose Y or N.")
    exit()

# Final bill
print(f"Your final bill is: ${bill}.")
