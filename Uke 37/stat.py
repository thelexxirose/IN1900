import numpy as np
import math


def mean(x_list):
    m = (1/len(x_list))*sum(x_list)
    return m


def test_mean():
    x_test_values = [0.699, 0.703, 0.698, 0.688, 0.701]
    expected = np.mean(x_test_values)
    computed = mean(x_test_values)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed mean={computed} != {expected}(expected)"
    assert success, msg


def standard_deviation(x_list):
    m = mean(x_list)
    s = 0
    for i in x_list:
        s += (i - m)**2

    res = math.sqrt((1/len(x_list)) * s)
    return res


def test_standard_deviation():
    x_test_values = [0.699, 0.703, 0.698, 0.688, 0.701]
    expected = np.std(x_test_values)
    computed = standard_deviation(x_test_values)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed mean={computed} != {expected}(expected)"
    assert success, msg


test_mean()
test_standard_deviation()

'''
(base) corybalaton@Corys-MacBook-Pro Uke 37 %
/Users/corybalaton/opt/anaconda3/bin/python
"/Users/corybalaton/Documents/UiO/IN1900/Uke 37/stat.py"
'''
