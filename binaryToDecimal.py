import sys
from math import pow

sum = 0
currPow = 0
debugMode = False

if (len(sys.argv) == 1):
    print("Requires a binary number to convert: \n$python3 binaryToDecimal.py [binaryNumber]")
    exit()
if (len(sys.argv) > 2):
    if (sys.argv[2] == "-d"):
        debugMode = True
if (sys.argv[1] == "-help"):
    print("Usage: binaryToDecimal.py [binaryNumber]")
    exit()
for i in range(len(sys.argv[1]) - 1, -1, -1):
    
    if not sys.argv[1][i] in "01":
        print("Error: \'" + sys.argv[1][i] + "\' \nMay only contain 0 or 1")
        exit()
    sum += int(sys.argv[1][i]) * pow(2, currPow)
    
    if debugMode:
        print("===============Debug==============")
        print("Input: " + sys.argv[1])
        print("Bit (" + str(i) + "): " + (sys.argv[1][i]))
        print("Current power: " + str(pow(2, currPow)))
        print("Current Sum: " + str(sum))
        print()
    
    currPow += 1
print("Decimal Output: " + str(sum))

