# Student Performance Trend Analysis

subjects = ["Maths", "Physics", "Python"]

exams = int(input("Enter number of examinations: "))

marks = []

# Read marks
for i in range(exams):
    print("\nExamination", i + 1)

    exam_marks = []

    for subject in subjects:
        score = float(input("Enter marks in " + subject + ": "))
        exam_marks.append(score)

    marks.append(exam_marks)


# Calculate subject-wise analysis
print("\n========== PERFORMANCE ANALYSIS ==========")

weak_subjects = []

for j in range(len(subjects)):

    subject_marks = []

    for i in range(exams):
        subject_marks.append(marks[i][j])

    average = sum(subject_marks) / exams

    print("\nSubject:", subjects[j])
    print("Average:", round(average, 2))

    # Improvement and decline
    for i in range(1, exams):
        change = marks[i][j] - marks[i - 1][j]

        if change > 0:
            print("Exam", i, "to Exam", i + 1,
                  ": Improved by", change)
        elif change < 0:
            print("Exam", i, "to Exam", i + 1,
                  ": Declined by", abs(change))
        else:
            print("Exam", i, "to Exam", i + 1,
                  ": No change")

    # Check consistently weak subject
    if all(score < 50 for score in subject_marks):
        weak_subjects.append(subjects[j])


# Overall average
total = 0
count = 0

for i in range(exams):
    for j in range(len(subjects)):
        total += marks[i][j]
        count += 1

overall_average = total / count


# Classification
if overall_average >= 75:
    classification = "Excellent"
elif overall_average >= 60:
    classification = "Good"
elif overall_average >= 50:
    classification = "Average"
else:
    classification = "Needs Improvement"


# Final result
print("\n========== FINAL RESULT ==========")
print("Overall Average:", round(overall_average, 2))
print("Classification:", classification)

if len(weak_subjects) > 0:
    print("Consistently Weak Subjects:", weak_subjects)
else:
    print("No consistently weak subjects.")
