def read_person_data(filename):
    with open(filename, "r") as f:
        d = {}
        for line in f:
            data = line.rstrip().split(",")
            d.update({data[0]: {"Age": data[1].strip(),
                                "Gender": data[2].strip()}})
    return d


def write_person_data(data_dict, filename):
    with open(filename, "w") as f:
        for key in data_dict:
            f.write(f"{key}, {data_dict[key]['Age']}, \
                {data_dict[key]['Gender']} \n")


d = read_person_data("people_dict.txt")
d.update({"Cory": {"Age": 20, "Gender": "Male"}})
write_person_data(d, "new_people_dict.txt")

'''
(base) corybalaton@eduroam-193-157-179-38 Uke 42 %
/Users/corybalaton/opt/anaconda3/bin/python
"/Users/corybalaton/Documents/UiO/IN1900/Uke 42/people_dict.py"
'''
