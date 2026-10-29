# Problem Statement
Develop a Python program to process examination marks for multiple subjects. The program should check each subject against its minimum pass mark, apply grace marks according to a specified grace-mark policy, ensure that marks never exceed the maximum marks, and finally display the student's result and classification.
# Algorithm
1. Start.
2. Read the number of subjects.
3. For each subject, read:
   - Subject name
   - Maximum marks
   - Obtained marks
   - Minimum pass marks
4. Check whether the obtained marks are greater than or equal to the pass mark.
5. If the student fails by a small margin, check whether the required grace marks are within the allowed grace limit.
6. Apply grace marks if permitted.
7. Ensure the final marks do not exceed the maximum marks.
8. Check the result of all subjects.
9. Calculate total marks and percentage.
10. Classify the student:
    - 75% and above → Distinction
    - 60%–74% → First Class
    - 50%–59% → Second Class
    - Below 50% → Pass
    - If any subject is still failed → Fail
11. Display the final result.
12. Stop.
# Mermaid Flowchart
```mermaid
flowchart TD
    A([Start]) --> B[Read number of subjects]
    B --> C[Set Pass Mark = 40 and Grace = 5]
    C --> D[Read subject marks]
    D --> E{Marks >= 40?}

    E -- Yes --> F[Subject Pass]
    E -- No --> G{Marks >= 35?}

    G -- Yes --> H[Calculate required grace marks]
    H --> I[Apply grace marks]
    I --> J{Final marks > 100?}
    J -- Yes --> K[Set marks = 100]
    J -- No --> L[Keep final marks]

    K --> M{Final marks >= 40?}
    L --> M
    M -- Yes --> F
    M -- No --> N[Subject Fail]

    F --> O{More subjects?}
    N --> O
    O -- Yes --> D
    O -- No --> P[Calculate Total and Percentage]
    P --> Q{Percentage >= 75?}
    Q -- Yes --> R[Distinction]
    Q -- No --> S{Percentage >= 60?}
    S -- Yes --> T[First Class]
    S -- No --> U{Percentage >= 50?}
    U -- Yes --> V[Second Class]
    U -- No --> W{All Subjects Passed?}
    W -- Yes --> X[Pass]
    W -- No --> Y[Fail]
    R --> Z([End])
    T --> Z
    V --> Z
    X --> Z
    Y --> Z
```
# sample input
Enter number of subjects: 5
Enter marks for Subject 1: 78
Enter marks for Subject 2: 65
Enter marks for Subject 3: 38
Enter marks for Subject 4: 82
Enter marks for Subject 5: 55
