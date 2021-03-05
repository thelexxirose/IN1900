def create_dict(filename):
    res = {}
    with open(filename, "r") as f:
        tmp = {}
        for idx, line in enumerate(f):
            tmp.update({idx: line})

    for i in range(1, len(tmp)):
        line = tmp[i].rstrip().replace(",", "").split(";")
        for j in line:
            el = j.split("-")
            res.update({el[0].strip().upper(): float(el[1].strip())})

    return res


print(create_dict("atm_moon.txt"))

'''
(base) corybalaton@eduroam-193-157-189-149 Uke 42 %
/Users/corybalaton/opt/anaconda3/bin/python
"/Users/corybalaton/Documents/UiO/IN1900/Uke 42/atm_moon.py"

{'HELIUM 4': 40000.0, 'NEON 20': 40000.0, 'HYDROGEN': 35000.0,
'ARGON 40': 30000.0, 'NEON 22': 5000.0, 'ARGON 36': 2000.0,
'METHANE': 1000.0, 'AMMONIA': 1000.0, 'CARBON DIOXIDE': 1000.0}
'''
