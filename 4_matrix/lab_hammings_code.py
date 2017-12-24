from mat import Mat
from matutil import listlist2mat
from GF2 import One

# Task 4.14.1 Create instance of Mat representing the generator matrix G
G = listlist2mat([[1, 0, 1, 1],
                  [1, 1, 0, 1],
                  [0, 0, 0, 1],
                  [1, 1, 1, 0],
                  [0, 0, 1, 0],
                  [0, 1, 0, 0],
                  [1, 0, 0, 0]])

print(G)



