def dna_complement(orig_strand):
    new_strand = ''
    for char in orig_strand:
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
    dna_complement("ATCG")


main()