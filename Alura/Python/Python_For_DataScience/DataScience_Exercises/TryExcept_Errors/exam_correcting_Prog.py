## Exercise 5

answers = ['D','A','B','C','A']
student_answers = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
student_answers_wEx = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

def grading(answer_sheet,student_answer):
    grade = 0
    grade_results = []
    for s in range(len(student_answer)):
        for a in range(len(answer_sheet)):
            if student_answer[s][a] not in answer_sheet:
                raise ValueError
            elif student_answer[s][a] == answer_sheet[a]:
                grade += 1
        grade_percent = (grade / len(answer_sheet)) * 10
        grade_results.append(grade_percent)
        grade = 0
    return grade_results

try:
    grades = grading(answers, student_answers)
    print(grades)
except ValueError:
    print("One of the answer inputs has an option not found in the answer sheet.")
                