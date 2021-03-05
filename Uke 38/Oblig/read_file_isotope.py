
isotope_list = open("text_files/oxygen.txt").readlines()

new_list = []

for line in isotope_list:
    new_list.append(line.split("\t"))

for i, line in enumerate(new_list):
    for j, el in enumerate(line):
        new_list[i][j] = el.strip()
    new_list[i] = [j for j in line if j]

M = 0
for i in range(1, len(new_list)):
    M += float(new_list[i][1]) * float(new_list[i][2])

print(f"M = {M:.4f} g/mol")

'''
(base) corybalaton@Corys-MacBook-Pro Oblig % /Users/corybalaton/opt/anaconda3/bin/python "/Users/corybalaton/Documents/UiO/IN1900/Uke 38/Oblig/read_file_isotope.py"
M = 15.9994 g/mol
'''
