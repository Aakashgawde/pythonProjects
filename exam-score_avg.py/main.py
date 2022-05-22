# entering how many exams you have done
number_of_exams = int(input("enter number of exams: "))

#! entering how many credits
total_credits = int(input("Enter how many credits these exams cover: "))

#! begin with avgerage of 0 then add up percentage from each exam
avg = 0
for exam in range(number_of_exams):
    score = int(input("Enter exams score: "))
    exam_credits = int(input("enter how many credits this exams covered: "))
    avg = avg + score * exam_credits/total_credits

print(f"Your average is {avg}")


