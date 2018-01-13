from math import sin, cos
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

# Task 4.15.4
def scale(alpha, beta):
    return Mat(({'y', 'u', 'x'}, {'y', 'u', 'x'}), {('x', 'x'): alpha, ('y', 'y'): beta, ('u', 'u'): 1})


# Task 14.15.5
def rotation(theta):
    return Mat(({'y', 'u', 'x'}, {'y', 'u', 'x'}),
               {('x', 'x'): cos(theta),
                ('x', 'y'): -sin(theta),
                ('y', 'x'): sin(theta),
                ('y', 'x'): cos(theta),
                ('u', 'u'): 1})


## Task 5
def rotate_about(theta, x, y):
    '''
    Input:  an angle theta (in radians) by which to rotate, and x- and y- coordinates of a point to rotate about
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
>>> (rotate_about(math.pi/3, 3,4)*Vec({'x','y','u'}, {'x':1, 'y':0, 'u':1}) - Vec({'y', 'x', 'u'},{'y': 0.26794919243112214, 'x': 5.4641016151377535, 'u': 1})).is_almost_zero()
    True
    '''
    pass

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.

    >>> reflect_y()*Vec({'x','y','u'}, {'x':1, 'y':1, 'u':1}) == Vec({'x','y','u'}, {'x':-1, 'y':1, 'u':1})
    True
    >>> reflect_y()* Vec({'x','y','u'}, {'u':1}) == Vec({'x','y','u'},{'u':1})
    True
    '''
    pass

## Task 7
def reflect_x():
    '''
    Input:  None.
    Output:  3x3 X-reflection matrix.

    >>> reflect_x()*Vec({'x','y','u'}, {'x':1, 'y':1, 'u':1}) == Vec({'x','y','u'}, {'x':1, 'y':-1, 'u':1})
    True
    >>> reflect_x()*Vec({'x','y','u'}, {'u':1}) == Vec({'x','y','u'},{'u':1})
    True
    '''
    pass

## Task 8
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.

    >>> scale_color(1,2,3)*Vec({'r','g','b'},{'r':1,'g':2,'b':3}) == Vec({'r','g','b'},{'r':1,'g':4,'b':9})
    True
    '''
    pass

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    pass

## Task 10
def reflect_about(x1, y1, x2, y2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.

    >>> (reflect_about(0,1,1,1) * Vec({'x','y','u'}, {'u':1}) - Vec({'x', 'u', 'y'},{'x': 0.0, 'u': 1, 'y': 2.0})).is_almost_zero()
    True
    >>> (reflect_about(0,0,1,1) * Vec({'x','y','u'}, {'x':1, 'u':1}) - Vec({'x', 'u', 'y'},{'u': 1, 'y': 1})).is_almost_zero()
    True
    '''
    pass
