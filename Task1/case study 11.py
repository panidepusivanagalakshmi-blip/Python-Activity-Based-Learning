# Examination Result and Grace-Mark Validation

n = int(input("Enter number of subjects: "))

grace_limit = 5
total_marks = 0
total_maximum = 0
failed = False

for i in range(n):
    print("\nSubject", i + 1)

    subject = input("Enter subject name: ")
    maximum = int(input("Enter maximum marks: "))
    marks = int(input("Enter obtained marks: "))
    pass_mark = int(input("Enter minimum pass marks: "))

    final_marks = marks

    # Check pass or apply grace marks
    if marks >= pass_mark:
        print(subject, "passed without grace marks.")

    else:
        grace_needed = pass_mark - marks

        if grace_needed <= grace_limit:
            final_marks = marks + grace_needed

            # Do not exceed maximum marks
            if final_marks > maximum:
                final_marks = maximum

            print("Grace marks applied:", grace_needed)
        else:
            failed = True
            print(subject, "failed. Grace marks cannot be applied.")

    # Final validation
    if final_marks < pass_mark:
        failed = True

    total_marks += final_marks
    total_maximum += maximum

    print("Final marks:", final_marks, "/", maximum)

# Calculate percentage
percentage = (total_marks / total_maximum) * 100

print("\n----- FINAL RESULT -----")
print("Total Marks:", total_marks, "/", total_maximum)
print("Percentage:", round(percentage, 2), "%")

# Classification
if failed:
    classification = "FAIL"
elif percentage >= 75:
    classification = "DISTINCTION"
elif percentage >= 60:
    classification = "FIRST CLASS"
elif percentage >= 50:
    classification = "SECOND CLASS"
else:
    classification = "PASS"

print("Classification:", classification)
