myfile = open("temp.txt", "r")
while(True):
    line = myfile.readline()
    if(len(line) == 0):
        break
    print(line, end="")
myfile.close()
            