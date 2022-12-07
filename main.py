def fCalc(inp, key):
    input1 = inp
    input2 = len(inp)
    output1 = ""
    list1 = [["-" for i in range(input2)] for j in range(key)]

    column = 0
    row = [i for i in range(key)]
    for i in range(key-2, 0, -1):
        row.append(i)

    while input1:
        for i in row:
            if column < input2:
                list1[i][column] = "nul"
                column += 1
                input1 = input1[1:]

    for i in range(key):
        for j in range(input2):
            if list1[i][j] == "nul":
                list1[i][j] = inp[0]
                inp = inp[1:]

    for i in range(input2):
        for j in range(key):
            if list1[j][i] != "-":
                output1 += list1[j][i]
    return output1


def fWriteOut(inp, key, down=2, top=10):
    if key >= 2:
        output1 = fCalc(inp, key)
        return output1

def fWriteRoot():
    val1 = input("Podaj tekst do szyfrowania/deszyfracji: ")
    klucz = int(input("Podaj klucz (liczba całkowita): "))
    if klucz >= 2:
            print("Tekst wyjściowy: ", fWriteOut(val1, klucz))
    else:
            print("Zły klucz")

fWriteRoot()