#Basic for loops
for x in "Python":
    print(x)
    print("\n")

array = [1,2,3]
for x in array:
    print(x)
    print("\n")

for x in range(10,16):
    print(x)
    print("\n")


for x in range(0,10,2):
    print(x) # 0 - 10 stepping by 2 (0,2,4,6,8)

#Object style for loop

names = ["Jordon", "John", "Mary"]
found = False
int_J_Names = 0

print("searching for a J name")
for name in names:
    if name.startswith("J"):
        print("Found")
        found = True
        int_J_Names += 1
        #break

if not found:
    print("No J names Found")
else:
    print("Found " + str(int_J_Names) + " J Names")
    print("Found " , int_J_Names, " J Names")
