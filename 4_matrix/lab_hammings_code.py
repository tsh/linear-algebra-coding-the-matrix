from mat import Mat
from matutil import listlist2mat
from vecutil import list2vec
from vec import dot
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

# Task 4.14.3
R = listlist2mat([[0, 0, 0, 0, 0, 0, One()],
                  [0, 0, 0, 0, 0, One(), 0],
                  [0, 0, 0, 0, One(), 0, 0],
                  [0, 0, One(), 0, 0, 0, 0]])

# Task 4.14.4
H = listlist2mat([[0, 0, 0, One(), One(), One(), One()],
                  [0, One(), One(), 0, 0, One(), One()],
                  [One(), 0, One(), 0, One(), 0, One()]])

# Task 4.14.5
def find_error(e):
    """ Takes error syndrome and return error vector """
    pos = dot(e, list2vec([1, 2, 4])) - 1
    err_vector = [0] * 7
    err_vector[pos] = 1
    return list2vec(err_vector)
