import sys

d = dict()
with open(sys.argv[1], "r") as file:
    data = file.readlines()
    for line in data:
        for i in line:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
with open("output.txt", "w") as file:
    for i, j in d.items():
        file.write("{}: {}\n".format(i, j))
    file.close()
