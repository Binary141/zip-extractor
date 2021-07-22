from zipfile import ZipFile
import os

def main():

    mylist = os.listdir()

    for file in mylist:
        if(file[len(file)-4:] == ".zip"):
            print(file)
            filename = file

            with ZipFile(filename, 'r') as zip:
                print('extracting ', filename)
                directory = "./" + filename[:len(file)-4]
                zip.extractall(directory)
                print('done!')

main()
