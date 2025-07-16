from textwrap import wrap


def find(sequence):
    # https://stackoverflow.com/questions/9475241/split-string-every-nth-character
    string = wrap(sequence, 3)
    start_codon = 'ATG'
    stop_codon = ('TAG', 'TAA', 'TGA')

    i = 0
    sequences = []
    while i < len(string):
        if string[i] == start_codon:
            sequence1 = ""
            print(sequence1)
            while i < len(string) and string[i] not in stop_codon:
                sequence1 += string[i]
                i += 1
            sequences.append(sequence1)

    print(sequences)


def complementary(sequence):
    new_strand = ''
    for char in sequence:
        match char:
            case 'A':
                new_strand += 'T'
            case 'T':
                new_strand += 'A'
            case 'C':
                new_strand += 'G'
            case 'G':
                new_strand += 'C'

    print(new_strand)


def main():
    # find(input("Enter a DNA sequence: "))
    find('ATGCGATAAGTGATGTAG')


main()