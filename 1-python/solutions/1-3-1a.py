#input
#numbers = [2,3,5,10]

#process
#total = sum(numbers)
#count = len(numbers)
#avg = total / count

#Output
#print(avg)

# Second step re-write program into function
def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return avg

numbers = [5,6]
grades = [ 100, 100, 100,0]
avg_grade = average(grades)
avg_numbers = average(numbers)
print(f"Average of {grades} is {avg_grade}")
print(f"Average of {numbers} is {avg_numbers}")


