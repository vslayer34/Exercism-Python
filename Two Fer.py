from helper import display_task_name, display_example


def two_fer(name: str = "you"):
    return f"One for {name}, one for me."



# Test 1
display_task_name("I", "TwoFer > no name given")

display_example(
    "two_fer()",
    "One for you, one for me."
)
print(two_fer(), "\n")



# Test 2
display_task_name("II", "TwoFer > a name given")

display_example(
    'two_fer("Alice")',
    "One for Alice, one for me."
)
print(two_fer("Alice"), "\n")



# Test 3
display_task_name("III", "TwoFer > another name given")

display_example(
    'two_fer("Bob")',
    "One for Bob, one for me."
)
print(two_fer("Bob"), "\n")