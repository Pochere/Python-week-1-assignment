# Defining the function that calculates the final price after applying a discount. 
def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        # Calculate the final price by reducing the discount amount
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Main program
# Prompting the user to enter the original price of an item and the discount percentage. 
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call the function to calculate the final price
    final_price = calculate_discount(price, discount_percent)

    # Output the results
    if final_price == price:
        print(f"No discount applied. The original price is: ${price:.2f}")
    else:
        print(f"The final price after applying the discount is: ${final_price:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values for price and discount percentage.")
