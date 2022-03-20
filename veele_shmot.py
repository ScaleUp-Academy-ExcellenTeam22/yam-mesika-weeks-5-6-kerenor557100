#submitted by Keren Or Hadad 208025205
from itertools import product


def veele_shmot(Fname, Lname, min_length= None):
    capitalized_Fname = [word.title() for word in Fname]
    capitalized_Lname = [word.title() for word in Lname]
    full_names = [a + " " + b for a, b in product(capitalized_Fname, capitalized_Lname)]
    if min_length is not None:
        full_names = [name for name in full_names if len(name) >= min_length]
    return full_names


first_names = ['avi', 'moshe', 'yaakov']
last_names = ['cohen', 'levi', 'mizrahi']
print(veele_shmot(first_names, last_names, 10))
print(veele_shmot(first_names, last_names))
"""
output:
['Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi', 'Moshe Mizrahi', 'Yaakov Cohen', 'Yaakov Levi', 'Yaakov Mizrahi']
['Avi Cohen', 'Avi Levi', 'Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi', 'Moshe Mizrahi', 'Yaakov Cohen', 'Yaakov Levi', 'Yaakov Mizrahi']
"""
