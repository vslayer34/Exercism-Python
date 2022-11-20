# helper function to help with display of tests
from helper import display_example, display_task_name

"""
Functions for organizing and calculating student exam scores.
https://exercism.org/tracks/python/exercises/making-the-grade
"""


def round_scores(student_scores: list):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    rounded_student_scores =[]
    for i in range(len(student_scores)):
        score = student_scores.pop()
        rounded_student_scores.append(round(score))

    return rounded_student_scores


def count_failed_students(student_scores: list):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    count = 0
    for score in student_scores:
        if score  <= 40:
            count += 1
    
    return count


def above_threshold(student_scores: list, threshold: int):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    excellent_score = []
    for score in student_scores:
        if score >= threshold:
            excellent_score.append(score)
    
    return excellent_score

def letter_grades(highest: int):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    list_of_grades_thresholds = []
    range_of_pass_grades = highest - 40
    interval_of_grades = range_of_pass_grades // 4
    for number in range(41, highest, interval_of_grades):
        list_of_grades_thresholds.append(number)
    return list_of_grades_thresholds



def student_ranking(student_scores: list, student_names: list):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    list_of_students = []
    for index, score in enumerate(student_scores):
        element = f"{index + 1}. {student_names[index]}: {score}"
        list_of_students.append(element)
    
    return list_of_students


def perfect_score(student_info: list):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for student in student_info:
        if student[1] == 100:
                index_of_student = student_info.index(student)
                return student_info[index_of_student]
    
    return []
    # return empty list if the loop didn't find anything to the condition to return




# Task I
display_task_name("I", "Rounding Scores")
student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
display_example("round_scores(student_scores)"
    , "[40, 39, 95, 80, 25, 31, 70, 55, 40, 90]")
print(round_scores(student_scores), "\n")



# Task II
display_task_name("II", "Non-Passing Students")
display_example("count_failed_students(student_scores=[90,40,55,70,30,25,80,95,38,40])", "5")
print(count_failed_students(student_scores=[90,40,55,70,30,25,80,95,38,40]), "\n")



# Task III
display_task_name("III", 'The "Best"')
display_example('above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75)', "[90, 75, 83, 96]")
print(above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75), "\n")



# Task IV
display_task_name("IV", "Calculating Letter Grades")
display_example("letter_grades(highest=100)", "[41, 56, 71, 86]")
print(letter_grades(100), "\n")

display_example("letter_grades(highest=88)", "[41, 53, 65, 77]")
print(letter_grades(88), "\n")



# Task V
display_task_name("V", "Matching Names to Scores")
student_scores = [100, 99, 90, 84, 66, 53, 47]
student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']
display_example("student_ranking(student_scores, student_names)"
    ,"['1. Joci: 100', '2. Sara: 99', '3. Kora: 90', '4. Jan: 84', '5. John: 66', '6. Bern: 53', '7. Fred: 47']")
print(student_ranking(student_scores, student_names), "\n")



# Task VI
display_task_name('VI', 'A "Perfect" Score')
display_example('perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]])', '["Alex", 100]')
print(perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]]), "\n")

display_example('perfect_score(student_info=[["Charles", 90], ["Tony", 80]])', '[]')
print(perfect_score(student_info=[["Charles", 90], ["Tony", 80]]), "\n")