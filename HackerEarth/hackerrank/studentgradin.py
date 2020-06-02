import math
import os
import random
import re
import sys
def gradingStudents(grades):
        mul=(grades/5)+1
        check=(mul*5)-grades
        if (check<2):
            grades=mul
            return grades
        else:
            return grades   

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
    
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
