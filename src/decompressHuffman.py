import huffman
from ast import literal_eval

def decompressHuff(filename):

    compressedFile = open(filename)
    uncompressedFile = open("uncompressedFile.txt", "w")

    lines = []

    for line in compressedFile:

        line.replace("\n", "")
        lines.append(line)

    dic = literal_eval(lines.pop())
    print dic
    splitLines = [x.split() for x in lines]

    for line in splitLines:

        uncompressedLine = ""

        for character in line:

            uncompressedLine += dic[character]

        uncompressedLine += " \n"

        uncompressedFile.write(uncompressedLine)



    compressedFile.close()
    uncompressedFile.close()

decompressHuff("new.txt")
