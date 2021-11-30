ALLOWED_NUCLEOTIDES = ['A', 'T', 'G', 'C']
COMPLEMENTARY_NUCLEOTIDES = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


class DnaFragment:
    def __init__(self, name=None, sequence=None):
        self.name = name
        self.sequence = sequence

    def get_name(self):
        return self.name

    def get_sequence(self):
        return self.sequence

    def incorrect_letters_found(self):
        for nucleotide in self.sequence:
            if nucleotide not in ALLOWED_NUCLEOTIDES:
                print(nucleotide)
                return True
        return False

    def get_reverse_complement(self):
        reverse_complement = ""
        for nucleotide in reversed(self.sequence):
            reverse_complement += COMPLEMENTARY_NUCLEOTIDES[nucleotide]
        return reverse_complement
