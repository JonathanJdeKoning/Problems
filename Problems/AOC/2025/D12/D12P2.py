from itertools import *
from collections import *
from heapq import *
from functools import *
ans = 0
A = []
with open("test2.in","r") as file:
#with open("data.in","r") as file:
    for i, line in enumerate(file.readlines()):
        l = line.strip().split()