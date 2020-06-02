import math
import os
import random
import re
import sys

def miniMaxSum(arr):

    a=sum(arr)
    print(a-max(arr),a-min(arr))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
