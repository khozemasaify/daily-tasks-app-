def task():
    tasks = [] #ALL TASKS
    print("------ Welcome To The Task Management App ------")
    total_task = int(input("Enter How Many Task You Want To Add : ")) #TASKS Number LISTS
    for i in range(1,total_task+1):
        task_name = input(f"Enter Task {i}=")
        tasks.append(task_name)
    print(f"Today's Tasks are \n{tasks}")
    print()
    #Crud operations of Task
    while True:
        operations = int(input(f"\nEnter 1-ADD Tasks \n2-Update Tasks \n3-Delete Tasks \n4-View Tasks \n5-Exit/Stop"))
        # Add Task
        if operations == 1: 
            add = input(f"\nEnter Task That You Want To Add = ")
            tasks.append(add)
            print(f"Task {add} has been added successfully")
        # Update Task
        elif operations == 2:
            update_val = input(f"\nEnter Task Name That You Want To Update = ")
            if update_val in tasks:
                updates = input("ENTER NEW TASK")
                indexing = tasks.index(update_val)
                tasks[indexing] = updates
                print(f"Task {updates} has been Updated successfully")
            else:
                print(f"Task {update_val}  not found in the list")
        # Delete Task
        elif operations == 3:
            delete_tasks = input(f"\nEnter Task Name That You Want To Delete = ")
            if delete_tasks in tasks:
                tasks.remove(delete_tasks)
                print(f"Task {delete_tasks} has been deleted successfully")
            else:
                print(f"Task {delete_tasks}  not found in the list")
        # View Task
        elif operations == 4:
            print(f"\nYour Current Tasks are : {tasks}")
        #Exit
        elif operations == 5:
            print(f"\nExiting Task Management App. Goodbye!")
            break
        else:
            print(f"\nInvalid Input {operations} Please enter a valid operation")
task()