from image_mat_util import file2mat, mat2display
from matutil import identity
from mat import Mat

# Task 4.15.4
# mat2display(*file2mat('img01.png'))

# Task 4.15.5
def identify():
    return Mat(({'y', 'u', 'x'}, {'y', 'u', 'x'}), {('x', 'x'): 1, ('y', 'y'): 1, ('u', 'u'): 1})
