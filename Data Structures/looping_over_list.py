#problem -1

letters = ["a","c","b"]

for index,letter in enumerate(letters,start=1):
    print(index,letter)

#problem - 2

runers = ["Martin","justin","guru"]

for position,runer in enumerate(runers,start=2):
    print(position,runer)

#problem -3

task_by_prority = ["Pay Rent","Buy Potato"]

for index,task in enumerate(task_by_prority):
    if index == 0:
        print(f"{task.upper()}")
    else:
        print(f"{task}")
