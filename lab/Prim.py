# Prim's Algorithm in Python
import sys
import math
import heapq
from turtle import distance


graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 3, 'D': 8},
    'C': {'A': 4, 'B': 3, 'E': 5, 'D': 2},
    'D': {'B': 8, 'C': 2, 'E': 11, 'F': 22},
    'E': {'C': 2, 'D': 11, 'F': 1},
    'F': {'D': 22, 'E': 1}
}