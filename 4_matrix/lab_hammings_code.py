from mat import Mat
from matutil import listlist2mat, mat2coldict, coldict2mat
from vecutil import list2vec
from bitutil import str2bits, bits2str, bits2mat, mat2bits, noise
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
H = listlist2mat([
                  [One(), 0, One(), 0, One(), 0, One()],
                  [0, One(), One(), 0, 0, One(), One()],
                  [0, 0, 0, One(), One(), One(), One()],
                  ])


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
    err_vector = [0] * 7
    pos = dot(list2vec(v), list2vec([1, 2, 4]))
    if pos:
        pos -= 1  # array from 0
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

# Task 4.14.8
s = ''.join([chr(i) for i in range(256)])
assert bits2str(str2bits(s)) == s

# Task 4.14.9 & 4.14.10 encode message string to matrix of nibbles
msg = "I'm trying to free your mind, Neo."
P = bits2mat(str2bits(msg))

# Task 4.14.11 add noise to message
E = noise(P, 0.02)
EP = E + P
perturbed_msg = bits2str(mat2bits(EP))

# Task 4.14.12
C = G*P

# Task 4.14.13
CE = noise(C, 0.02)
CTILDE = C + CE
perturbed_msg2 = bits2str(mat2bits(R*CTILDE))

# Task 4.13.13
def correct(A):
    return R * (find_error_matrix(H*A) + A)

