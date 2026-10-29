# Progressive Electricity Billing

fixed_charge = 100
surcharge_rate = 0.10
rebate_rate = 0.05

bills = []
units_list = []

n = int(input("Enter number of months: "))

for month in range(1, n + 1):

    print("\nMonth", month)
    units = float(input("Enter electricity consumption in units: "))

    # Calculate energy charge using progressive slabs
    if units <= 100:
        energy_charge = units * 2

    elif units <= 200:
        energy_charge = (100 * 2) + ((units - 100) * 3)

    elif units <= 300:
        energy_charge = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    else:
        energy_charge = (100 * 2) + (100 * 3) + (100 * 5) + ((units - 300) * 7)

    bill = energy_charge + fixed_charge

    surcharge = 0
    rebate = 0

    # Apply surcharge
    if units > 300:
        surcharge = bill * surcharge_rate
        bill = bill + surcharge

    # Apply rebate
    elif units < 100:
        rebate = bill * rebate_rate
        bill = bill - rebate

    bills.append(bill)
    units_list.append(units)

    print("Energy Charge: ₹", round(energy_charge, 2))
    print("Fixed Charge: ₹", fixed_charge)
    print("Surcharge: ₹", round(surcharge, 2))
    print("Rebate: ₹", round(rebate, 2))
    print("Final Bill: ₹", round(bill, 2))

    # Compare with previous month
    if month > 1:
        previous_bill = bills[month - 2]

        increase = ((bill - previous_bill) / previous_bill) * 100

        print("Change from Previous Month:", round(increase, 2), "%")

        if increase > 20:
            print("Warning: Unusual increase in bill!")
        else:
            print("Bill increase is normal.")


# Final Summary
print("\n----- ELECTRICITY BILL SUMMARY -----")

for i in range(n):
    print("Month", i + 1,
          "- Units:", units_list[i],
          "- Bill: ₹", round(bills[i], 2))

print("\nHighest Bill: ₹", round(max(bills), 2))
print("Lowest Bill: ₹", round(min(bills), 2))
