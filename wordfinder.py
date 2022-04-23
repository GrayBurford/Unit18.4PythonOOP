"""Word Finder: finds random words from a dictionary."""
import random

# 18.3 Video #15 FILES

class WordFinder:
    """
    Class method for outputting a random word from a given list of words in a file.
    """
    def __init__(self, file):
        """
        Counts words in a given file and returns # of words read
        """
        self.file = file
        self.all_text = open(file, "r")
        self.parsed_words = self.parse_file(self.all_text)
        print(f'{len(self.parsed_words)} words read')

    def __repr__(self):
        return f'Reading text from WordFinder({self.file})'        

    def parse_file(self, all_text):
        """
        Parses TextIOWrapper to list of words read.
        """
        # for word in all_text.readlines():
        #     self.parsed_words.append(word)
        # self.parsed_words = set(self.parsed_words)
        # return self.parsed_words.words()

        return [word for word in all_text.readlines()]


        # In [53]: new_list[3][0:-1]
        # Out[53]: 'abaiser'

    def random(self):
        """
        Returns random word generated from given list of words.
        """
        # open(self.file, "r")
        # return random.choice([1,2,3,4,5])
        rand_word = random.choice(self.parsed_words)
        return rand_word[0:-1]

class SpecialWordFinder(WordFinder):
    """
    From parent class WordFinder: "Class method for outputting a random word from a given list of words in a file." but excludes lines that are blank, and lines that start with a "#"
    """
    def parse_file(self, all_text):
        """
        Parses TextIOWrapper to list of words read.
        """
        return [word for word in all_text.readlines() if word.strip() and not word.startswith("#")]