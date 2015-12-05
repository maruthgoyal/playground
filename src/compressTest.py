import huffman


def main():

    f = open("lorem.txt")

    newFile = open("new.txt", "w")

    otherFile = open("otherFile.txt", "w")


    for line in f:

        line = line.replace("\n", "")

        a = huffman.huffmanEncodedStr(line)
        nLine = a[0] +  " " + "\n"

        newFile.write(nLine)

        otherFile.write(''.join(format(ord(x), 'b') for x in line))
        print nLine

    newFile.write("\n")
    newFile.write(str(a[1]))

    f.close()
    newFile.close()
    otherFile.close()

if __name__ == '__main__':
    main()
