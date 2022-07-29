student_scores = input("Scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_value= 0
for number in student_scores:
    if number > highest_value:
        highest_value = number
print(f"The highest value is {highest_value}")
