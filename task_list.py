tasks = [
    {"description": "Wash Dishes",
     "completed": False,
     "time_taken": 10
     },
    {"description": "Clean Windows", "completed": False, "time_taken": 15},
    {"description": "Make Dinner", "completed": True, "time_taken": 30},
    {"description": "Feed Cat", "completed": False, "time_taken": 5},
    {"description": "Walk Dog", "completed": True, "time_taken": 60},
]


# Print a list of uncompleted tasks
print("A list of uncompleted tasks:")
uncompleted_tasks = []
for task in tasks:
    if task["completed"] == False:
        uncompleted_tasks.append(task["description"])

for task in uncompleted_tasks:
    print(f"{task}")
print()


# Print a list of completed tasks
print("A list of completed tasks:")
completed_tasks = []
for task in tasks:
    if task["completed"] == True:
        completed_tasks.append(task["description"])

for task in completed_tasks:
    print(f"{task}")
print()


# Print a list of all task descriptions
print("List of task descriptions: ")
for task in tasks:
    print(task["description"])
print()


# Print a list of tasks where time_taken is at least a given time
print("Tasks that took longer than 15 minutes: ")
longer_tasks = []
for task in tasks:
    if task["time_taken"] >= 15:
        longer_tasks.append(task["description"])

for task in longer_tasks:
    print(f"{task}")
print()


# Print any task with a given description
task_to_search = input("Search for a task: ")
found_task = None
for task in tasks:
    if task["description"].lower() == task_to_search.lower():
        found_task = task
if found_task != None:
    print(found_task)
else:
    print("Task not found")
print()



# Extension
# Given a description, update that task to mark it as complete.
description_to_search_for = input("Search for a task, to update as completed: ")
found_description = False
for task in tasks:
    if task["description"].lower() == description_to_search_for.lower():
        found_description = True
        if task["completed"] == False:
            task["completed"] = True
            print("The following task has now been completed:")
            print(task)
        elif task["completed"] != False:
            print("That task is already completed.")
        # elif task["description"].lower() != description_to_search_for.lower():
        #     print("Task does not exist")

print()


# #  Add a task to the list
print("Adding a new task to the list.")
new_task_name = input("Enter a task name: ")
new_task_completed = input("Enter if this task is complete. (True/False) ")
new_task_time = input("How many minutes will this take? ")

new_task = {"description": new_task_name, "completed": new_task_completed , "time_taken": new_task_time}
tasks.append(new_task)

print("An updated list of tasks: ")
print(tasks)

print()