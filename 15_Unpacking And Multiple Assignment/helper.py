# function for displaying the output and the examples
def display_task_name(num: str, headline: str):
    formated_text = f"Task {num}: {headline}"
    print(formated_text)
    print("-" * len(formated_text))

def display_example(function: str, output: str):
    print(function)
    print("EX output:", output)
    print("My output: ", end="")