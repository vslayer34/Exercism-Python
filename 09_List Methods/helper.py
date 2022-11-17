# function for displaying the output and the examples
def display_task_name(num: str, headline: str):
    print("Task", num + ":", headline)
    print("_______________________________")

def display_example(function: str, output: str):
    print(function)
    print("EX output:", output)
    print("My output: ", end="")