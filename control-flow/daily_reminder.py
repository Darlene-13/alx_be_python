# Enter your daily task and its priority level
Task = input('What is your task for today?')
Priority = input('What is the priority level of thsis task? (high/medium/low): ').lower()
Time_bound = input('Is this task time-bound? (yes/no?)')

# Match case to react based on priority level
match Priority:

    case 'high':
        if Time_bound == 'yes':
            print(f"Your task {Task} is of high priority and it is time-bound. Make sure to complete it first.")
        else:
            print(f" Your task {Task} is of high priority. Make sure to complete it first.")
    case 'medium':
        if Time_bound == 'yes':
            print(f"Your task {Task} is of medium priority and it is time-bound. You can complete it after high priority tasks.")
        else:
            print(f"Your task {Task} is of medium priority. You can complete it after high priority tasks.")
    case 'low':
        if Time_bound =='yes':
            print("However, since it is time-bound, make sure to complete it on time.")
        else:
            print(f" Your task {Task} is of low priority. You can complete it later.")
    case _:
        print('Invalid priority level.Please enter high, medium or low.')