# University Scholarship Allocation

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")

    m1 = int(input("Enter marks in Subject 1: "))
    m2 = int(input("Enter marks in Subject 2: "))
    m3 = int(input("Enter marks in Subject 3: "))

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter family income: "))

    total = m1 + m2 + m3
    aggregate = (total / 300) * 100

    if (aggregate >= 75 and
        m1 >= 60 and m2 >= 60 and m3 >= 60 and
        attendance >= 75 and income <= 500000):

        students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

# Ranking
students.sort(
    key=lambda x: (-x["aggregate"],
                   -x["attendance"],
                   x["income"])
)

print("\n----- SCHOLARSHIP ELIGIBLE STUDENTS -----")

if len(students) == 0:
    print("No students are eligible for the scholarship.")
else:
    rank = 1

    for student in students:
        print("\nRank:", rank)
        print("Name:", student["name"])
        print("Aggregate:", round(student["aggregate"], 2), "%")
        print("Attendance:", student["attendance"], "%")
        print("Family Income: ₹", student["income"])

        rank += 1
