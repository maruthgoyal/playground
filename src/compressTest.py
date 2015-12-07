import huffman

uncompressedFile = open("hel.txt")
compressedFile = open("compressed.txt", "w")
appearanesOfLineBreak = []
oneLine = ''

for line in uncompressedFile:

    oneLine += line


for i in xrange(len(oneLine)):

    if oneLine[i] == "\n":

        appearanesOfLineBreak.append(i)

appearanesOfLineBreak = appearanesOfLineBreak[::-1]

compressedString = huffman.huffmanEncodedStr(oneLine)

compressSplit = compressedString.split()

index = 0

if appearanesOfLineBreak:

    while appearanesOfLineBreak:

        newLine = ''
        lineBreakIndex = appearanesOfLineBreak.pop()

        for i in xrange(index, lineBreakIndex):

            newLine += (compressSplit[i] + ' ')

        index = lineBreakIndex + 1
        newLine += "\n"
        compressedFile.write(newLine)

else:

    compressedFile.write(compressedString)

dic = huffman.getDic()


compressedFile.write(str(dic))

compressedFile.close()
uncompressedFile.close()
