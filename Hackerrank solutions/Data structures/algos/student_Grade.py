import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    next_near = [5*((x//5) + 1) for x in grades]
    diff = [next_near[i]-grades[i] for i in range(len(grades))]
    new_grades = [next_near[i] if diff[i] < 3 and next_near[i]>=40 
                  else grades[i] for i in range(len(grades)) ]
    #print(next_near)
    #print(diff)
    #print(new_grades)
    return new_grades

if __name__ == '__main__':
    
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)