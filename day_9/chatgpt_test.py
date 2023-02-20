tasks = []

while True:
    print("Enter a task (or 'q' to quit):")
    task = input()
    if task == 'q':
        break
    tasks.append(task)

print("Here is your to-do list:")
for task in tasks:
    print("- " + task)