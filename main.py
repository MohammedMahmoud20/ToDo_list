massage = """1.Add new task
2.Display all tasks
3.Mark task as complete
4. Exit"""

tasks = []
completed_task=[]

def add_task(task_name):
  tasks.append(task_name)
  print("task added to the list succesfully ")

def mark_completed_tasks(completed_tasks):
  tasks.pop(completed_tasks-1)
  completed_task.append(completed_tasks-1)
  print("task compeleted succesfully ")

def display_tasks():
  if len(tasks)>0:
    counter=0
    print("incompeleted tasks : ")
    for i , task in enumerate(tasks):
         print(f"{i+1}-{task} ❌")
         counter+=1
    print("completed tasks : ")
    for i , task in enumerate(completed_task,start=counter):
         print(f"{i+1}-{task} ✔️")
         counter+=1
  else:
    print("there is no tasks ")
    return

while True:
  print(massage)
  choice = input("Enter your choice ")
  if isinstance(choice, str):
    if choice == "1":
      name = input("enter your task ")
      add_task(name)
    elif choice == "3":
      if len(tasks)==0:
        print("congratulation, all tasks completed ")
        break
      if len(tasks)>0:
        for i , task in enumerate(tasks):
         print(f"{i+1}-{task}")
      completed_tasks = input("enter the task you want to mark as complete ")
      mark_completed_tasks(int(completed_tasks))
    elif choice == "2":
      display_tasks()
    elif choice == "4":
      break
    else:
      print("please enter a valid choice ")