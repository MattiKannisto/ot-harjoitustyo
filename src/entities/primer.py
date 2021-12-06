class Primer:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

    def get_name(self):
        return self.name

    def get_sequence(self):
        return self.sequence

    def get_length(self):
        return len(self.sequence)
