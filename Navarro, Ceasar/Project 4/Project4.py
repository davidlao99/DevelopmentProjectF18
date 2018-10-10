f = open(r"C:\Users\Ceasar\Desktop\Fall2018 Projects\DevelopmentProjectF18\Navarro, Ceasar\Project 4\randomInts.txt","r")
a = []
for line in f:
    a.append(int(line))
b = len(a)
print(a)
print(b)
f.close()