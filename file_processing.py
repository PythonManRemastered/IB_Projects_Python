import os 

if os.path.exists("numbers.txt") == False:
    print("The file does not initially exist. This program will now create it.")


def file_writer(string):
    try:
        f = open("numbers.txt",'a')
        f.write(string)
        f.close()
    except:
        return "An error has occured while writing to the file"


def file_reader(string):
    if string.lower() == "all":
        f = open("numbers.txt", 'r')
        x = None
        try:
            while x != "":
                x = f.readline()
                print(x)
        except:
            f.close()
            return "An error has occured while reading the file"

file_writer("\n Albanian cuisine is delicious!")
file_reader("all")