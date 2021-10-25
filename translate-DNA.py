""" This program translates genes to proteins. """

def translate(DNA_Sequence, codonTable):

    ### Find ATG codon before we start constructing the protein sequence
    TRANSLATING = False
    sequence = ""
    for i in range(0,len(DNA_Sequence), 3):
        codon = DNA_Sequence[i:i+3]

        if TRANSLATING:
            char = codonTable.get(codon)
            if char == "stop":
                break
            else:
                sequence += char

        ### ATG has been found, so start translating the protein sequence
        if codon == "ATG":
            TRANSLATING = True

    return sequence


    """ Complete the second-half of the translate function, which will take
        the current codon and append its translation to the protein sequence.
        Be sure to check if you hit a stop codon (the stop codons are not in
        the dictionary); break the loop if you have.
    """



def readCodons(filename):
    """ Complete the readCodons() function to add entries to the dictionary.
        Each line of the file has one amino acid and then all of the codons
        that map to it. Each codon/amino-acid pair will need to be in the
        dictionary. Note: the three letter abbreviation of the amino acid
        appears first, followed by the one-letter abbreviation, followed by all
        of the codons that map to it.
    """
    infile = open(filename, 'r')
    codonTable = {}
    for line in infile:
        line = line.strip()
        line = line.split(",")
        amino = line[1]
        codons = line[2:]
        for codon in codons:
            # make codon, amino key-value pair and add key-value pair to list
            codonTable[codon] = amino
    return codonTable


def readDNAFile(filename):
    infile = open(filename, 'r')
    sequence = ""
    for line in infile:
        if line[0] != ">":
            sequence += line.strip()
    infile.close()
    return sequence


def main():

    filename = str(input("Enter filename: "))

    DNA_Sequence = readDNAFile(filename)
    codonTable = readCodons("codon.txt")
    # print(codonTable.items())

    translated_sequence = translate(DNA_Sequence, codonTable)
    print("DNA sequence:\n%s" % DNA_Sequence)
    print("Translated protein sequence:\n%s" % translated_sequence)


main()
