import huffman

"""
Tests the huffman.py by using it to encode an entire file and then writing the compressed
data to another file, "compressed.txt"

"""

def main():

    uncompressedFile = open("lorem.txt") # The uncompressed file.
    compressedFile = open("compressed.txt", "w") # The new file we'll be writing to.

    appearanesOfLineBreak = [] # A list that stores the indices of all the line breaks
    oneLine = '' # A single line string to which all the lines in the uncompressed file will be appended

    for line in uncompressedFile: # Adding each line in the uncompressed file to 'oneLine'

        oneLine += line


    print oneLine

    for i in xrange(len(oneLine)): # Checking for line breaks (\n) and storing their index.

        if oneLine[i] == "\n":

            appearanesOfLineBreak.append(i)

    appearanesOfLineBreak = appearanesOfLineBreak[::-1] # Done to make using the pop() operation a bit easier later on (Also a bit of optimization)

    compressedString = huffman.huffmanEncodedStr(oneLine) # Compress the oneLine ( to rule them all :p)


    compressSplit = compressedString.split() # Get each character in the compressedString

    index = 0 # Helps keep track during list slicing

    if appearanesOfLineBreak: # Checking whether there are any line breaks

        while appearanesOfLineBreak: # while the list of line breaks is not empty ("The Pythonista way")

            newLine = '' # The new line to be written to the compressed file.
            lineBreakIndex = appearanesOfLineBreak.pop() # index of a line break

            for i in xrange(index, lineBreakIndex): # from index upto but not including lineBreakIndex

                newLine += (compressSplit[i] + ' ') # Add the respective compressed character and a space (provides seperation since chars are variable length)

            index = lineBreakIndex + 1 # Set index to be the one after the line break
            newLine += "\n" # Basically, hitting Enter.
            compressedFile.write(newLine) # writing our line to the new file

    else: # If no line breaks, just write the string to the file

        compressedFile.write(compressedString)

    dic = huffman.getDic() # Get a dictionary that maps compressed character values to the respective character generated by the huffman encoder.


    compressedFile.write(str(dic)) # Write the dictionary to the end of the file for uncompressing purposes.

    compressedFile.close() # close the file
    uncompressedFile.close() # close the file

if __name__ == '__main__':
    main()
