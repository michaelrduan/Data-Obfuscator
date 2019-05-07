import json
import os
import random
from collections import namedtuple

sensitive = {"SSN", "Address", "Name", "Phone"}

'''
Input: filename
Output: print the contents of json
Change Later: parse through all files in a folder
'''

def get_file():
    direc = os.getcwd()
    direc += "/input_files"

    files = []
    for filename in os.listdir(direc):
        if filename.endswith(".json"):
            files.append(filename)


    return files



def open_file(fname, ofile):
    with open(fname) as json_data:
        data = json.load(json_data)


    for data1 in data:
        for k, v in data1.items():
            if k in sensitive:
                new_v = randomizer(k)
                data1[k] = new_v



    with open(ofile, 'w') as outfile:
        json.dump(data, outfile, indent = 4)





def randomizer(key):
    if key == "SSN":
        return random_ssn()
    elif key == "Name":
        return random_name()
    elif key == "Address":
        return random_address()
    elif key == "Phone":
        return random_phone()





def random_ssn():
    #"SSN": "484-70-4050",
    first = ""
    for i in range(3):
        first += str(random.randint(0,9))
    first += "-"
    for i in range(2):
        first += str(random.randint(0,9))
    first += "-"
    for i in range(3):
        first += str(random.randint(0,9))
    return first



def random_name():
    first = ["John", "Carol", "Jacob", "Jose", "Arman", "Sang"]
    last = ["Wang", "Smith", "Gomez", "Fisher", "Bryant", "James"]

    name = first[random.randint(0, len(first) - 1)] + " " + last[random.randint(0,len(last)- 1)]
    return name



def random_address():
    return "123 Memory Lane"


def random_phone():
    first = ""
    for i in range(3):
        first += str(random.randint(0, 9))
    first += "-"
    for i in range(4):
        first += str(random.randint(0, 9))
    first += "-"
    for i in range(4):
        first += str(random.randint(0, 9))
    return first




def main():
    '''
    file = raw_input("Enter first file name (w/ .json): ")
    path  = os.getcwd()
    folder = "/input_files"
    fp = path + folder + "/" + file
    print(fp)
    '''

    #this is list of all json files
    files = get_file()
    print(files)
    print("above is files")

    fp = "/Users/michaelduan/Documents/Side Things/Side Projects/input_files/data50.json"

    for f in files:
        direc = os.getcwd()
        direc += "/input_files/" + f
        out_name = "obs_" + f
        open_file(direc, out_name)
    #open_file(fp, out_name)





if __name__ == "__main__":
    main()
