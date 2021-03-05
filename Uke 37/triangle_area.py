def test_triangle_area():
    """
    Verify the area of a triangle with vertices
    (0,0), (1,0), and (0,2).
    """
    v1 = [0, 0]
    v2 = [1, 0]
    v3 = [0, 2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success, msg


def triangle_area(v):
    A = (1/2)*abs(v[1][0]*v[2][1] - v[2][0]*v[1][1] - v[0][0]*v[2]
                  [1] + v[2][0]*v[0][1] + v[0][0]*v[1][1] - v[1][0]*v[0][1])
    return A


test_triangle_area()

'''
(base) corybalaton@Corys-MacBook-Pro Uke 37 %
/Users/corybalaton/opt/anaconda3/bin/python
"/Users/corybalaton/Documents/UiO/IN1900/Uke 37/triangle_area.py"
'''
