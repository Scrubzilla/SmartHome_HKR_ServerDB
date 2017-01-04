commandList = ["11000", "11100", "12000", "12200", "13000", "14000", "15000", "16000", "17000", "18000", "19000", "21000", "22000", "25000", "26000", "27000", ]

#if "110002".find(commandList) in commandList:
 #   print("dsssss")
'''
for i in range(0, len(commandList)):
    if "120" in commandList[i]:
        print("match")
        break
    else:
        print("no match")'''

commandList = ["11000", "11100", "12000", "12200", "13000", "14000", "15000", "16000", "17000", "18000", "19000",
               "21000", "22000", "25000", "26000", "27000", ]

for i in range(0, len(commandList)):
    if commandList[i] in "160":
        print("true")
        break
    print("false")