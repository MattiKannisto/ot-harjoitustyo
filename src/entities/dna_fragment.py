class DnaFragment:
    def __init__(self, name=None, sequence=None):
        self.name = name
        self.sequence = sequence

    def string_to_list(self, string):
        character_list = []
        for character in string:
            character_list.append(character)
        return character_list

    def get_name(self):
        return self.name

    def get_sequence(self):
        return self.sequence

    def incorrect_letters_found(self):
        adenosides = self.count_nucleotides(self.sequence, 'A')
        thymines = self.count_nucleotides(self.sequence, 'T')
        guanines = self.count_nucleotides(self.sequence, 'G')
        cytosines = self.count_nucleotides(self.sequence, 'C')
        return (adenosides + thymines + guanines + cytosines) != len(self.sequence)

    def count_nucleotides(self, dna_sequence, nucleotide):
        return dna_sequence.count(nucleotide)

    def get_reverse_complement(self):
        reverse_complement = ""
        for nucleotide in reversed(self.sequence):
            complementary_nucleotide = self.get_complementary_nucleotide(nucleotide)
            reverse_complement += complementary_nucleotide
        return reverse_complement

    def get_complementary_nucleotide(self, nucleotide):
            if nucleotide == 'A':
                return 'T'
            elif nucleotide == 'T':
                return 'A'
            elif nucleotide == 'G':
                return 'C'
            elif nucleotide == 'C':
                return 'G'
            else:
                return "ERROR"