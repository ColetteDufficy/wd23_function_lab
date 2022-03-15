tasks = [
    { "description": "Wash Dishes", 
     "completed": False, 
     "time_taken": 10 
     },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


# Print a list of uncompleted tasks      
uncompleted_tasks = []
for task in tasks:
    if task["completed"] == False:
        uncompleted_tasks.append(task["description"])
print(f"List of uncompleted tasks: {uncompleted_tasks}") 
print()

     
# Print a list of completed tasks      
completed_tasks = []
for task in tasks:
    if task["completed"] == True:
        completed_tasks.append(task["description"])
print(f"List of completed tasks: {completed_tasks}") 
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
print(longer_tasks)  
print()




        # print("Searching for a book by title...")
        # search_title = input("Enter title: ")
        # found_book = None
        # for book in library["books"]:
        #     if book["title"].lower() == search_title.lower():
        #         found_book = book
        # if found_book != None:
        #     title = found_book["title"]
        #     author = found_book["author"]
        #     print(f"Found {title} by {author}")
        # else:
        #     print(f"{search_title} not found")
