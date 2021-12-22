import sys
import os
li = {}
li2 = {}
li3 = []
for i in os.walk(f"Path\\To\\Folder"):
    for j in i[2]:
        li[j] = i[0]
for k in os.walk(f"Path\\To\\Folder2"):
    for l in k[2]:
        li2[l] = k[0]
if len(li2.keys()) > len(li.keys()):
    for z in li2.keys():
        if z not in li.keys():
            li3.append(f"{li2[z]}" + "\\" + f"{z}")
        else:
            pass
else:
    for z in li.keys():
        if z not in li2.keys():
            li3.append(f"{li[z]}" + "\\" + f"{z}")
        else:
            pass
print(len(li3))
sys.stdout = open("output.txt", "w", encoding="utf-8")
print(li3)
sys.stdout.close()