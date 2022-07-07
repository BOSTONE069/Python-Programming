import random

numList = []

for i in range(5):
    numList.append(random.randrange(1, 10))

i = len(numList) - 1

while i > 1:
    j = 0

    while j < i:

        print("\nIs {} > {}".format(numList[j], numList[j + 1]))

        if numList[j] > numList[j + 1]:

            print("Switch")

            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp
        else:
            print("Dont Switch")

        j += 1

        for k in numList:
            print(k, end=", ")
        print()

    print("END OF ROUND")

    i -= 1

for k in numList:
    print(k, end=", ")
print()
