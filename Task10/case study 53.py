# Food Waste Monitoring System

acceptable_limit = 10

total_prepared = 0
total_served = 0
total_leftover = 0

waste_days = []
results = []

n = int(input("Enter number of days: "))

for day in range(1, n + 1):

    print("\nDay", day)

    prepared = int(input("Enter meals prepared: "))
    served = int(input("Enter meals served: "))

    # Validate input
    if prepared <= 0 or served < 0 or served > prepared:
        print("Invalid input! Enter valid meal quantities.")
        continue

    leftover = prepared - served
    wastage = (leftover / prepared) * 100

    total_prepared += prepared
    total_served += served
    total_leftover += leftover

    if wastage > acceptable_limit:
        status = "Excessive Waste"
        waste_days.append(day)
    else:
        status = "Acceptable Waste"

    results.append((day, prepared, served, leftover,
                    wastage, status))

    print("Leftover Meals:", leftover)
    print("Wastage Percentage:", round(wastage, 2), "%")
    print("Status:", status)


# Final Summary
print("\n===== FOOD WASTE SUMMARY =====")

for result in results:
    print("\nDay:", result[0])
    print("Prepared:", result[1])
    print("Served:", result[2])
    print("Leftover:", result[3])
    print("Wastage:", round(result[4], 2), "%")
    print("Status:", result[5])

if total_prepared > 0:
    overall_wastage = (total_leftover / total_prepared) * 100
else:
    overall_wastage = 0

print("\nTotal Meals Prepared:", total_prepared)
print("Total Meals Served:", total_served)
print("Total Leftover Meals:", total_leftover)
print("Overall Wastage:", round(overall_wastage, 2), "%")

if len(waste_days) > 0:
    print("Days Exceeding Limit:", waste_days)
else:
    print("No days exceeded the wastage limit.")
