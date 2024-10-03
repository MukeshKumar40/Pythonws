# Function to convert Dollar to Rupees
def dollar_to_rupees(dollars, exchange_rate):
    return dollars * exchange_rate

# Function to convert Rupees to Dollar
def rupees_to_dollar(rupees, exchange_rate):
    return rupees / exchange_rate

# Main code
print("1. Convert Dollar to Rupees")
print("2. Convert Rupees to Dollar")

choice = int(input("Enter your choice (1 or 2): "))

# Assuming 1 Dollar = 83 Rupees (you can update the rate)
exchange_rate = 83.0

if choice == 1:
    dollars = float(input("Enter amount in dollars: "))
    print(f"{dollars} Dollar(s) = {dollar_to_rupees(dollars, exchange_rate)} Rupees")
elif choice == 2:
    rupees = float(input("Enter amount in rupees: "))
    print(f"{rupees} Rupee(s) = {rupees_to_dollar(rupees, exchange_rate)} Dollar(s)")
else:
    print("Invalid choice!")