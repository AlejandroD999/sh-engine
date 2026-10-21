from spellchecker import SpellChecker

class QueryProcessor:
    def __init__(self, query):
        self.query = query
        self.checker = SpellChecker(language="en")
        
        self.run()

    def spell_check(self, split_query):
        long_word_length = 7


        for idx, word in enumerate(split_query):
            # Toggle check distance: according to word length
            self.checker.distance = 2 if len(word) <= long_word_length else 1

            if word not in self.checker:
                corr_word = self.checker.correction(word)

                if corr_word:
                    split_query[idx] = corr_word
        
        return split_query
        

    
    def run(self):
        # Transforms and filters query
        split_query = input("Query: ").split() 

        corrected = self.spell_check(split_query)

        print(corrected)


if __name__ == "__main__":
    qp = QueryProcessor("Sofe gey wjo runs")
