import numpy as np


def extract_data(filename):
    f = open(filename).read()
    split_f = f.split()
    return split_f


oct_1945 = extract_data("temp_october_1945.txt")
oct_2014 = extract_data("temp_october_2014.txt")

print(f"{' '.join(oct_1945[:6])} <==> minimum temp: {min(oct_1945[6:])} <==> \
    maximum temp: {max(oct_1945[6:])} <==> average temp: \
        {np.mean(np.array(oct_1945[6:]).astype(np.float)):.6f}")
print(f"{' '.join(oct_2014[:6])} <==> minimum temp: {min(oct_2014[6:])} <==> \
    maximum temp: {max(oct_2014[6:])} <==> average temp: \
        {np.mean(np.array(oct_2014[6:]).astype(np.float)):.6f}")


def write_formatting(filename, list1, list2):
    f = open(filename, "w")
    for i in range(6, len(list1)):
        f.write(f"{float(list1[i]):2.1f} <==> {float(list2[i]):2.1f}")
        f.write("\n")


write_formatting("temp_formatted.txt", oct_1945, oct_2014)


'''
(base) corybalaton@Corys-MacBook-Pro Uke 39 %
/Users/corybalaton/opt/anaconda3/bin/python
"/Users/corybalaton/Documents/UiO/IN1900/Uke 39/temp_read_write.py"

Year: 1945. Month: October. Location: Blindern(Oslo). <==>
minimum temp: 10.8 <==> maximum temp: 9.6 <==> average temp: 6.506452

Year: 2014. Month: October. Location: Blindern(Oslo). <==>
minimum temp: 10.3 <==> maximum temp: 9.8 <==> average temp: 8.854839
'''
