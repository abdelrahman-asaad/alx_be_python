# daily_reminder.py

# Get user input for task, priority, and time sensitivity
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Optional: Validate input (loop until valid input is given)
valid_priorities = ["high", "medium", "low"]
while priority not in valid_priorities:
    print("Please enter a valid priority: high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

while time_bound not in ["yes", "no"]:
    print("Please enter 'yes' or 'no' for time-bound.")
    time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide customized reminder using match-case (Python 3.10+ required)
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Make sure to schedule it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Plan to do it this week.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task, but it is time-sensitive. Try to complete it today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
