import math as m


def f(x):
    ans = m.sin(x)
    if(ans > 0):
        return ans
    else:
        return 0


def test_half_wave():
    expected_1 = 0
    computed_1 = f(4)
    tol = 1E-14
    success_1 = abs(expected_1 - computed_1) < tol
    msg = f"computed number={computed_1} != {expected_1}(expected)"
    expected_2 = m.sin(2)
    computed_2 = f(2)
    success_2 = abs(expected_2 - computed_2) < tol
    msg = f"computed number={computed_2} != {expected_2}(expected)"

    assert success_1, msg
    assert success_2, msg


test_half_wave()

'''
(base) corybalaton@Corys-MacBook-Pro Uke 37 %
/Users/corybalaton/opt/anaconda3/bin/python
"/Users/corybalaton/Documents/UiO/IN1900/Uke 37/half_wave.py"
'''
