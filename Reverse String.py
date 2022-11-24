from helper import display_task_name, display_example

def reverse(text: str) -> str:
    return text[::-1]





display_task_name("I", "Reverse a string")
display_example(
    'reverse("cool")',
    'looc'
)

print(reverse("cool"))