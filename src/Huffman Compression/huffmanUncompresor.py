from ast import literal_eval

lines = []

compressedFile = open("compressed.txt")
uncompressedFile = open("uncompressedFile.txt", 'w')

for line in compressedFile:

    a = line.replace('\n', '')
    lines.append(a)

dic = literal_eval(lines.pop()) # Dictionary of character mappings

splitLines = [x.split() for x in lines]

for line in splitLines:

    uncompressedLine = ''

    for character in line:

        uncompressedWord = dic[character]

        uncompressedLine += uncompressedWord

    uncompressedLine += '\n'
    uncompressedFile.write(uncompressedLine)

compressedFile.close()
uncompressedFile.close()
