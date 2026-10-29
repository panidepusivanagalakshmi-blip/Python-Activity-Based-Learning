# Retail Billing with Multiple Discount Rules

discount_rate = 0.10
discount_threshold = 5000
maximum_discount = 1000

total_subtotal = 0
total_discount = 0
total_tax = 0
grand_total = 0

invoice = []

n = int(input("Enter number of products: "))

for i in range(1, n + 1):

    print("\nProduct", i)

    name = input("Enter product name: ")
    category = input("Enter category (electronics/clothing/food): ").lower()
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    subtotal = price * quantity

    # Category-specific tax
    if category == "electronics":
        tax_rate = 0.18
    elif category == "clothing":
        tax_rate = 0.05
    elif category == "food":
        tax_rate = 0.00
    else:
        tax_rate = 0.10

    # Threshold discount
    if subtotal >= discount_threshold:
        discount = subtotal * discount_rate

        # Maximum concession limit
        if discount > maximum_discount:
            discount = maximum_discount
    else:
        discount = 0

    taxable_amount = subtotal - discount
    tax = taxable_amount * tax_rate
    final_amount = taxable_amount + tax

    total_subtotal += subtotal
    total_discount += discount
    total_tax += tax
    grand_total += final_amount

    invoice.append([
        name,
        category,
        quantity,
        subtotal,
        discount,
        tax,
        final_amount
    ])


# Display Invoice
print("\n========== ITEMIZED INVOICE ==========")

for item in invoice:
    print("\nProduct:", item[0])
    print("Category:", item[1])
    print("Quantity:", item[2])
    print("Subtotal: ₹", round(item[3], 2))
    print("Discount: ₹", round(item[4], 2))
    print("Tax: ₹", round(item[5], 2))
    print("Final Amount: ₹", round(item[6], 2))

print("\n========== BILL SUMMARY ==========")
print("Total Subtotal: ₹", round(total_subtotal, 2))
print("Total Discount: ₹", round(total_discount, 2))
print("Total Tax: ₹", round(total_tax, 2))
print("Grand Total: ₹", round(grand_total, 2))
