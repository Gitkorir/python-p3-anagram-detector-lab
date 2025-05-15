# your code goes here!
class Anagram:

    def __init__(self,word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self,items ):
        matches =[]
        for item in items: 
            if item.lower() != self.word and sorted(item.lower()) == self.sorted_word:
                matches.append(item)
        return matches   