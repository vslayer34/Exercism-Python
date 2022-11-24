from helper import display_task_name, display_example



def leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    else:
        return False




# Test 1
display_task_name("I", "Leap > year not divisible by 4 in common year")
display_example(
    "leap_year(2015)",
    "False"
)
print(leap_year(2015), "\n")



# Test 2
display_task_name("II", "Leap > year divisible by 2 not divisible by 4 in common year")
display_example(
    "leap_year(1970)",
    "False"
)
print(leap_year(1970), "\n")



# Test 3
display_task_name("III", "Leap > year divisible by 4 not divisible by 100 in leap year")
display_example(
    "leap_year(1996)",
    "True"
)
print(leap_year(1996), "\n")



# Test 4
display_task_name("IV", "Leap > year divisible by 4 and 5 is still a leap year")
display_example(
    "leap_year(1960)",
    "True"
)
print(leap_year(1960), "\n")



# Test 5
display_task_name("V", "Leap > year divisible by 100 not divisible by 400 in common year")
display_example(
    "leap_year(2100)",
    "False"
)
print(leap_year(2100), "\n")



# Test 6
display_task_name("VI", "Leap > year divisible by 100 but not by 3 is still not a leap year")
display_example(
    "leap_year(1900)",
    "False"
)
print(leap_year(1900), "\n")



# Test 7
display_task_name("VII", "Leap > year divisible by 400 is leap year")
display_example(
    "leap_year(2000)",
    "True"
)
print(leap_year(2000), "\n")



# Test 8
display_task_name("VIII", "Leap > year divisible by 400 but not by 125 is still a leap year")
display_example(
    "leap_year(2400)",
    "True"
)
print(leap_year(2400), "\n")



# Test 9
display_task_name("IX", "Leap > year divisible by 200 not divisible by 400 in common year")
display_example(
    "leap_year(1800)",
    "False"
)
print(leap_year(1800), "\n")