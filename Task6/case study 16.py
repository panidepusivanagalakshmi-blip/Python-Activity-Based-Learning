# Multi-Day Water Tank Simulation

capacity = 10000
water_level = 5000
minimum_level = 1000
threshold = 8000

overflow_count = 0
shortage_count = 0
first_threshold_interval = -1

n = int(input("Enter number of intervals: "))

for i in range(1, n + 1):

    print("\nInterval", i)

    inflow = float(input("Enter inflow in litres: "))
    outflow = float(input("Enter outflow in litres: "))

    # Update water level
    water_level = water_level + inflow - outflow

    # Check overflow
    if water_level > capacity:
        overflow = water_level - capacity
        overflow_count += 1
        print("Overflow:", overflow, "litres")
        water_level = capacity
    else:
        print("No overflow.")

    # Check shortage
    if water_level < minimum_level:
        shortage_count += 1
        print("Warning: Water shortage!")
    else:
        print("No shortage.")

    # Check threshold
    if water_level >= threshold and first_threshold_interval == -1:
        first_threshold_interval = i
        print("Threshold reached for the first time.")

    print("Water Level:", water_level, "litres")


# Final Summary
print("\n========== WATER TANK SUMMARY ==========")
print("Final Water Level:", water_level, "litres")
print("Total Overflow Intervals:", overflow_count)
print("Total Shortage Intervals:", shortage_count)

if first_threshold_interval != -1:
    print("First Threshold Reached at Interval:",
          first_threshold_interval)
else:
    print("Threshold was not reached.")
