# Problem Statement
Design a Python program to evaluate students for a university scholarship based on aggregate marks, subject-wise minimum marks, attendance, and family income. The program should identify eligible students, rank them according to their aggregate marks, and resolve ties using attendance and then family income.

Eligibility criteria:
- Aggregate marks ≥ 75%
- Minimum 60 marks in every subject
- Attendance ≥ 75%
- Family income ≤ ₹5,00,000
- If two students have the same aggregate, the student with higher attendance gets the higher rank.
- If both aggregate and attendance are the same, the student with lower family income gets the higher rank.
# Algorithm
1. Start.
2. Read the number of students.
3. For each student, read:
   - Student name
   - Marks in 3 subjects
   - Attendance percentage
   - Family income
4. Calculate the total marks and aggregate percentage.
5. Check whether the student:
   - Has aggregate ≥ 75%.
   - Has at least 60 marks in every subject.
   - Has attendance ≥ 75%.
   - Has family income ≤ ₹5,00,000.
6. If all conditions are satisfied, add the student to the eligible list.
7. Sort eligible students:
   - Higher aggregate first.
   - If aggregate is equal, higher attendance first.
   - If attendance is equal, lower income first.
8. Assign ranks to eligible students.
9. Display the ranked scholarship-eligible students.
10. Stop.
11. #Mermaid Flowchart
12. ```mermaid
    flowchart TD
    A([Start]) --> B[Read number of students]
    B --> C[Read student details]
    C --> D[Read marks in 3 subjects]
    D --> E[Calculate total and aggregate]
    E --> F[Read attendance and family income]

    F --> G{Aggregate >= 75?}
    G -- No --> H[Not Eligible]
    G -- Yes --> I{All subjects >= 60?}

    I -- No --> H
    I -- Yes --> J{Attendance >= 75?}

    J -- No --> H
    J -- Yes --> K{Income <= 500000?}

    K -- No --> H
    K -- Yes --> L[Add student to eligible list]

    H --> M{More students?}
    L --> M

    M -- Yes --> C
    M -- No --> N[Sort eligible students]

    N --> O[Higher aggregate gets higher rank]
    O --> P[If tie, higher attendance gets higher rank]
    P --> Q[If tie, lower income gets higher rank]
    Q --> R[Display ranked eligible students]
    R --> S([End])
    ```
    # sample input
    Enter number of students: 4

Student 1
Enter student name: Ravi
Enter marks in Subject 1: 85
Enter marks in Subject 2: 80
Enter marks in Subject 3: 90
Enter attendance percentage: 88
Enter family income: 350000

Student 2
Enter student name: Sita
Enter marks in Subject 1: 90
Enter marks in Subject 2: 85
Enter marks in Subject 3: 85
Enter attendance percentage: 82
Enter family income: 400000

Student 3
Enter student name: Arun
Enter marks in Subject 1: 75
Enter marks in Subject 2: 70
Enter marks in Subject 3: 80
Enter attendance percentage: 78
Enter family income: 450000

Student 4
Enter student name: Priya
Enter marks in Subject 1: 92
Enter marks in Subject 2: 88
Enter marks in Subject 3: 90
Enter attendance percentage: 90
Enter family income: 600000
    
