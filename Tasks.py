tasks = []

def exit_program():
    print("Programmist väljumine.")
    exit()


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task was added")


def view_tasks():
    if not tasks:
        print("Task list is empty")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter number of element"))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' was removed")
            else:
                print("Wrong number")
        except ValueError:
            print("Enter a number")



def user_speaker():
    while exit:
        exit = True
        print("\nHow Can I help you? Here is the menu: ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Tasks")
        print("4. Exit")


        choice = int(input("Choose an item (1-4): "))

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            exit_program()
        else:
            exit == False

    user_speaker()


    

    #def view_tasks():

    #def delete_task():

    #def exit_program():