import os
import sys
def timeConversion(s):
    
    if s[:2]=='12' and s[-2:]=='AM':
        return '00' +s[2:-2]
    if s[-2:]=='PM':
        return str(int(s[:2])+12) + s[2:-2]
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
