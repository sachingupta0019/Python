#################################################
##############  To Do List App  #################
#################################################

# class ToDoList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self):
#         print("Add tasks to the list or enter 'done' to exit:")
#         while True:
#             user_input = input("Task: ")
#             if user_input.lower() == 'done':
#                 print("Task List:", self.tasks)
#                 break
#             else:
#                 self.tasks.append(user_input)
#                 print(f"Added: {user_input}")

#     def remove_task(self):
#         if not self.tasks:
#             print("No tasks to remove.")
#             return
        
#         print("Tasks:", self.tasks)
#         while True:
#             task = input("Enter the task to remove or type 'done' to cancel: ")
#             if task.lower() == 'done':
#                 print("No changes made.")
#                 break
#             elif task in self.tasks:
#                 self.tasks.remove(task)
#                 print(f"Removed: {task}")
#                 print("Updated Task List:", self.tasks)
#             else:
#                 print(f"Task '{task}' not found. Please try again.")

#     def view_tasks(self):
#         if not self.tasks:
#             print("No tasks in the list.")
#         else:
#             print("Current tasks:", self.tasks)

# todo_list = ToDoList()
# todo_list.add_task()
# todo_list.view_tasks()
# todo_list.remove_task()
# todo_list.view_tasks()


class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self):
        print("Enter Task or Enter 'ok' to Exit : ")
        while True:
            task = input("Task : ")
            if task.lower() == 'ok':
                print('Task List : ', self.tasks)
                break
            else:
                self.tasks.append(task)
                print("Added Task : ", task)

    def remove_task(self):
        if not self.tasks:
            print("No Task to remove")
            return
        # print("Task List : ", self.tasks)
        while True:
            task = input("Enter Task to remove or enter 'ok' to cancel.\n")
            if task.lower() == 'ok':
                print('Updated Task List : ', self.tasks)
                print('No changes made.')
                return
            elif task in self.tasks:
                self.tasks.remove(task)
                print("Removed Task : ", task)
                print('Updated Task List : ', self.tasks)
            else:
                print("Task not present in list. Try Again!")
                

todo_list = ToDoList()
todo_list.add_task()
todo_list.remove_task()