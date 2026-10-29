# Advanced Numeric Pattern Generator

print("1. Hollow Diamond")
print("2. Symmetric Number Pyramid")

choice = int(input("Enter your choice (1 or 2): "))
size = int(input("Enter pattern size: "))

# Validate choice
if choice not in [1, 2]:
    print("Invalid choice!")

# Validate dimensions
elif size <= 0:
    print("Invalid size! Enter a positive integer.")

elif choice == 1 and (size < 3 or size % 2 == 0):
    print("Hollow diamond requires an odd size >= 3.")

else:
    print("\nGenerated Pattern:\n")

    if choice == 1:
        # Hollow diamond
        mid = size // 2

        for i in range(mid + 1):
            print(" " * (mid - i), end="")

            if i == 0:
                print("*")
            else:
                print("*" + " " * (2 * i - 1) + "*")

        for i in range(mid - 1, -1, -1):
            print(" " * (mid - i), end="")

            if i == 0:
                print("*")
            else:
                print("*" + " " * (2 * i - 1) + "*")

    else:
        # Symmetric number pyramid
        if size > 9:
            print("For clear alignment, use a size from 1 to 9.")
        else:
            for i in range(1, size + 1):
                print(" " * (size - i), end="")

                for j in range(1, i + 1):
                    print(j, end="")

                for j in range(i - 1, 0, -1):
                    print(j, end="")

                print()
