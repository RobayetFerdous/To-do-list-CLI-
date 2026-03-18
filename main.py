# add tasks
# view tasks
# marks tasks as done / next update
# delete tasks
# save tasks (so they don't disappear) / next update

tasks_list = []

def add_task():
    user_input = input("Enter your task: ")
    tasks_list.append(user_input)

def view_task():
    for i in range(len(tasks_list)):
        print(f"{i+1}. {tasks_list[i]}")

def delete_task():
    del tasks_list[-1]

#main
x = "y"
while x == "y":
    print("1. add tasks")
    print("2. view tasks")
    print("3. delete tasks")

    i = int(input("Select an option: "))

    match i:
        case 1:
            add_task()
        case 2:
            view_task()
        case 3:
            delete_task()
    
    x = input("Do you want to run TO DO list again? (y/n)")