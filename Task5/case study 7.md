# Problem Statement
Design a Python program to generate an itemized retail invoice for multiple products. The program should calculate the cost based on product price and quantity, apply category-specific taxes, provide threshold-based discounts, and ensure that the total discount does not exceed the maximum concession limit.

Assumptions:
- Electronics → 18% tax
- Clothing → 5% tax
- Food → 0% tax
- If item subtotal ≥ ₹5,000 → 10% discount
- Maximum discount allowed per item = ₹1,000
- Final amount = Subtotal − Discount + Tax
# Algorithm
1. Start.
2. Read the number of products.
3. Set tax rates for different categories.
4. Set the discount percentage and maximum concession limit.
5. For each product:
   - Read product name, category, price, and quantity.
6. Calculate the item subtotal:
   - Subtotal = Price × Quantity
7. Check whether the subtotal reaches the discount threshold.
8. If eligible, calculate the discount.
9. If discount exceeds ₹1,000, limit it to ₹1,000.
10. Calculate the taxable amount.
11. Apply the category-specific tax.
12. Calculate the final amount.
13. Add the values to the invoice total.
14. Display the itemized invoice.
15. Display total subtotal, discount, tax, and final bill.
16. Stop.
# Mermaid Flowchart
```mermaid
flowchart TD
    A([Start]) --> B[Read Number of Products]
    B --> C[Set Tax Rates and Discount Rules]
    C --> D[Read Product Name, Category, Price and Quantity]

    D --> E[Calculate Subtotal = Price x Quantity]
    E --> F{Subtotal >= 5000?}

    F -- Yes --> G[Calculate 10% Discount]
    F -- No --> H[Discount = 0]

    G --> I{Discount > 1000?}
    I -- Yes --> J[Set Discount = 1000]
    I -- No --> K[Keep Calculated Discount]

    J --> L[Calculate Taxable Amount]
    K --> L
    H --> L

    L --> M[Apply Category-Specific Tax]
    M --> N[Calculate Final Amount]
    N --> O[Add to Invoice Total]

    O --> P{More Products?}
    P -- Yes --> D
    P -- No --> Q[Display Itemized Invoice]
    Q --> R[Display Total Discount, Tax and Final Bill]
    R --> S([End])
```
# sample input
Enter number of products: 3

Product 1
Enter product name: Laptop
Enter category (electronics/clothing/food): electronics
Enter price: 50000
Enter quantity: 1

Product 2
Enter product name: Shirt
Enter category (electronics/clothing/food): clothing
Enter price: 1500
Enter quantity: 2

Product 3
Enter product name: Rice
Enter category (electronics/clothing/food): food
Enter price: 1000
Enter quantity: 6
