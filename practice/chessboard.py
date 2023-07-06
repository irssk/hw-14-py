sharp = "#"
space = " "
breakP = "\n"

def build(row, col):
    string = ""
 
    for i in range(row):
        if i % 2 == 0:
            for j in range(col):
                if j % 2 == 0:
                    string += sharp
                else:
                    string += space
 
            string += breakP
 
        else:
            for j in range(col):
                if j % 2 == 0:
                    string += space
                else:
                    string += sharp
 
            string += breakP
 
    return string

print(build(4, 8))