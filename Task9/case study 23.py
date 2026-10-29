# Student Timetable Conflict Detection

# Tuple format: (course, day, start, end, room)
# Time is represented in 24-hour HH:MM format.

timetable = [
    ("Python", "Monday", "09:00", "10:00", "R101"),
    ("Maths", "Monday", "10:00", "11:00", "R102"),
    ("Physics", "Tuesday", "09:00", "10:30", "R101"),
    ("English", "Monday", "11:00", "12:00", "R103")
]


def to_minutes(time):
    hours, minutes = map(int, time.split(":"))

    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        return -1

    return hours * 60 + minutes


print("Existing Timetable:")
for course in timetable:
    print(course)

print("\nEnter Proposed Class Details")

name = input("Course name: ")
day = input("Day: ").capitalize()
start = input("Start time (HH:MM): ")
end = input("End time (HH:MM): ")
room = input("Room: ")

start_min = to_minutes(start)
end_min = to_minutes(end)

conflicts = []

# Validate time
if start_min == -1 or end_min == -1 or start_min >= end_min:
    print("\nInvalid time interval.")
else:
    for course in timetable:
        old_name, old_day, old_start, old_end, old_room = course

        old_start_min = to_minutes(old_start)
        old_end_min = to_minutes(old_end)

        # Check whether periods overlap
        overlap = (
            start_min < old_end_min
            and end_min > old_start_min
        )

        if day == old_day and overlap:
            conflicts.append(
                "Schedule conflict with " + old_name
            )

        if room == old_room and overlap:
            conflicts.append(
                "Room " + room + " is unavailable due to "
                + old_name
            )

    print("\n----- TIMETABLE VALIDATION -----")

    if len(conflicts) == 0:
        print("Timetable is valid.")
        print("Proposed class can be scheduled.")
    else:
        for conflict in conflicts:
            print(conflict)

        print("Timetable is invalid.")
