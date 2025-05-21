#Variables
grades = [6.0,7.2,6.6,8.0,9.5]
bonus = 0.5

#Example 01
weighted_average = lambda x, y, z: (x * 3 + y * 2 + z * 5)/10
student_average = (weighted_average(grades[0],grades[1],grades[2]))
print(f'{student_average:.2f}')


#Example 02
updated_grades = map(lambda x: x + bonus, grades)
updated_grades = list(updated_grades)

print(updated_grades)