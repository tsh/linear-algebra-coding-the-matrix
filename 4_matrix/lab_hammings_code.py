from mat import Mat
from matutil import listlist2mat, mat2coldict, coldict2mat
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


def gf2_to_decimal(gf2_vec):
    """ Helper for 4.14.6; convert GF2 vector to decimal. """
    vec = [0] * len(gf2_vec.f)
    for pos, val in gf2_vec.f.items():
        vec[pos] = 1 if isinstance(val, One) else 0
    return vec


# Task 4.14.5
def find_error(e):
    """ Takes error syndrome and return error vector """
    v = gf2_to_decimal(e)
    pos = dot(list2vec(v), list2vec([1, 2, 4])) - 1
    err_vector = [0] * 7
    err_vector[pos] = One()
    return list2vec(err_vector)


# Task 4.14.6 Derive original message from [1, 0, 1, 1, 0, 1, 1]
non_c = list2vec([One(), 0, One(), One(), 0, One(), One()])
syndrome = H*non_c
e = find_error(syndrome)
codeword = e + non_c
message = R * codeword

# Task 4.14.7
def find_error_matrix(s):
    return coldict2mat({pos: find_error(vec) for pos, vec in mat2coldict(s).items()})

test_matrix = listlist2mat([[One(), 0], [One(), 0], [One(), One()]])
print(find_error_matrix(test_matrix))