elements_10 = {
    1: "-",
    2: "Helium",
    3: "Lithium",
    4: "Beryllium",
    5: "Boron",
    6: "Carbon",
    7: "Nitrogen",
    8: "-",
    9: "Fluorine",
    10: "Neon"
}

# a)

elements_10[1] = "Hydrogen"
elements_10[8] = "Oxygen"

# b)

# elements_10_copy is a copy of the elements_10 dict,
# so it wont't affect elements_10.
elements_10_copy = elements_10.copy()
elements_10_copy.update({11: "Sodium"})
print(elements_10)
print("\n")
# elements_11 is a reference to the elements_10 dict,
# so modifying elements_11 is going to directly modify
# elements_10
elements_11 = elements_10
elements_11.update({11: "Sodium"})
print(elements_10)


'''
(base) corybalaton@eduroam-193-157-179-38 Uke 42 %
/Users/corybalaton/opt/anaconda3/bin/python
"/Users/corybalaton/Documents/UiO/IN1900/Uke 42/chemical_elements_dict.py"

{1: 'Hydrogen', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5: 'Boron',
6: 'Carbon', 7: 'Nitrogen', 8: 'Oxygen', 9: 'Fluorine', 10: 'Neon'}


{1: 'Hydrogen', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium',
5: 'Boron', 6: 'Carbon', 7: 'Nitrogen', 8: 'Oxygen',
9: 'Fluorine', 10: 'Neon', 11: 'Sodium'}
'''
