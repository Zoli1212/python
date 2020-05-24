myfile = open("temp.txt", "r")
while(True):
    line = myfile.readline()
    if(len(line) == 0):
        break
    print(line, end="")
myfile.close()

print("")
print("")
myfile = open("temp.txt", "r")
linelist = myfile.readlines()
myfile.close()
for l in linelist:
    print(l, end="")