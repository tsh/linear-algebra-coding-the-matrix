from mat import Mat
from matutil import listlist2mat
from GF2 import One

# Task 4.14.1 Create instance of Mat representing the generator matrix G
G = listlist2mat([[One(), 0, One(), One()],
                  [One(), One(), 0, One()],
                  [0, 0, 0, One()],
                  [One(), One(), One(), 0],
                  [0, 0, One(), 0],
                  [0, One(), 0, 0],
                  [One(), 0, 0, 0]])

print(G)



