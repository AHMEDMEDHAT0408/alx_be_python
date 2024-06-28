task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

if priority == "high" and time_bound == "yes":
    print("Reminder: '" + task + "' is a high priority task that requires immediate attention today!")
elif priority == "high" and time_bound == "no":
    print("Reminder: '" + task + "' is a high priority task. Consider completing it when you have free time.")
elif priority == "medium" and time_bound == "yes":
    print("Reminder: '" + task + "' is a medium priority task that should be done soon.")
elif priority == "medium" and time_bound == "no":
    print("Reminder: '" + task + "' is a medium priority task. Try to complete it when possible.")
elif priority == "low" and time_bound == "yes":
    print("Reminder: '" + task + "' is a low priority task but is time-bound. Try to complete it today.")
elif priority == "low" and time_bound == "no":
    print("Note: '" + task + "' is a low priority task. Consider completing it when you have free time.")
