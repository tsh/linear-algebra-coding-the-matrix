from mat import Mat
from matutil import listlist2mat
from vecutil import list2vec
from GF2 import One

# Task 4.14.1 Create instance of Mat representing the generator matrix G
G = listlist2mat([[One(), 0, One(), One()],
                  [One(), One(), 0, One()],
                  [0, 0, 0, One()],
                  [One(), One(), One(), 0],
                  [0, 0, One(), 0],
                  [0, One(), 0, 0],
                  [One(), 0, 0, 0]])

# Task 4.14.2 what is the encoding of the message [1,0,0,1]
p = list2vec([One(), 0, 0, One()])
encoded_p = G * p
print(encoded_p)

# Task 4.14.3
R = listlist2mat([[0, 0, 0, 0, 0, 0, One()],
                  [0, 0, 0, 0, 0, One(), 0],
                  [0, 0, 0, 0, One(), 0, 0],
                  [0, 0, One(), 0, 0, 0, 0]])

# Task 4.14.4
H = listlist2mat([[0, 0, 0, One(), One(), One(), One()],
                  [0, One(), One(), 0, 0, One(), One()],
                  [One(), 0, One(), 0, One(), 0, One()]])


