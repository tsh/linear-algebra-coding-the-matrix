from image_mat_util import file2mat, mat2display
from mat import Mat

# Task 4.15.4
# mat2display(*file2mat('img01.png'))


def test_mat(m):
    data, color = file2mat('img01.png')
    mat2display(m*data, color)


# Task 4.15.5
def identity():
    return Mat(({'y', 'u', 'x'}, {'y', 'u', 'x'}), {('x', 'x'): 1, ('y', 'y'): 1, ('u', 'u'): 1})


# Task 4.15.3
def translation(alpha, beta):
    I = identity()
    I.f.update({('x', 'u'): alpha, ('y', 'u'): beta, ('u', 'u'): 1})
    return I


def scale(alpha, beta):
    return Mat(({'y', 'u', 'x'}, {'y', 'u', 'x'}), {('x', 'x'): alpha, ('y', 'y'): beta, ('u', 'u'): 1})