"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Finding random words from text database."""

    def __init__(self,txtFile):
        file = open(txtFile,"r")
        self.wordslist = [listing.strip() for listing in file]
        file.close

    def random(self):
        return random.choice(self.wordslist)

class SpecialWordFinder():
    """Finding random words, but skip search line start with '#' for comment"""

    def __init__(self,txtFile):
        file = open(txtFile,"r")
        self.wordslist = [listing.strip() for listing in file if not listing.startswith('#') and not "" ]
        file.close

    def random(self):
        return random.choice(self.wordslist)